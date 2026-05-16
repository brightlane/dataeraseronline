/**
 * Zero-Dependency Edge Ingest & Webhook Routing Engine
 * Target: Receives form payloads, validates format, and dispatches to CRM webhooks.
 * Runtime Environment: Node.js (v18+) / Edge Compatible
 */

const http = require('http');

// Configuration Matrix
const PORT = process.env.PORT || 3000;
const EXTERNAL_CRM_WEBHOOK = "https://your-automation-endpoint.com/catch/leads";

/**
 * Validates basic structural format of inbound emails
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length < 254;
}

/**
 * Handles incoming HTTP Request stream data safely
 */
function parseJsonBody(req) {
    return new Promise((resolve, reject) => {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
            // Flood protection: drop connections exceeding 1MB payload
            if (body.length > 1e6) { req.destroy(); reject(new Error("Payload too large")); }
        });
        req.on('end', () => {
            try {
                resolve(JSON.parse(body || '{}'));
            } catch (err) {
                reject(new Error("Invalid JSON structure"));
            }
        });
    });
}

/**
 * Central Server Handler Definition
 */
const server = http.createServer(async (req, res) => {
    // Enable CORS for static frontends (like GitHub Pages)
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    // Handle preflight requests gracefully
    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    // Enforce POST route handling exclusively
    if (req.method === 'POST' && req.url === '/v1/leads') {
        try {
            const data = await parseJsonBody(req);
            const { email, source, campaign } = data;

            // Inbound sanity check
            if (!email || !isValidEmail(email)) {
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ status: "error", message: "Malformed or invalid email parameter." }));
                return;
            }

            console.log(`[INGEST] Received valid lead registration: ${email}`);

            // Asynchronous dispatch to external CRM or Webhook engine
            const webhookPayload = JSON.stringify({
                email,
                lead_source: source || "Direct_Static_Lander",
                campaign_id: campaign || "Default_Campaign_2026",
                processed_at: new Date().toISOString()
            });

            // Fire-and-forget execution to avoid blocking client redirect loops
            fetch(EXTERNAL_CRM_WEBHOOK, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: webhookPayload
            }).catch(err => console.error("⚠️ Background Webhook Sync Failure:", err.message));

            // Return instantaneous success code so the front-end can execute redirect loops
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ status: "success", message: "Lead queued successfully." }));

        } catch (error) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ status: "error", message: error.message }));
        }
    } else {
        res.writeHead(444); // No Response / Drop route
        res.end();
    }
});

// Activate listener loop
server.listen(PORT, () => {
    console.log(`==================================================`);
    console.log(`📡 LEAD INGEST SERVER ACTIVE ON PORT: ${PORT}`);
    console.log(`==================================================`);
});
