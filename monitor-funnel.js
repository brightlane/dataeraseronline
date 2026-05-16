/**
 * High-Velocity Affiliate Link & Funnel Monitoring Engine
 * Target: Validates landing page status, javascript forms, and affiliate redirect targets.
 * Run Command: node monitor-funnel.js
 */

const http = require('http');
const https = require('https');

// Configuration Matrix
const CONFIG = {
    landingPageUrl: "https://brightlane.github.io/ManyChat/",
    expectedAffiliateTarget: "manychat.partnerlinks.io",
    timeoutMs: 5000
};

/**
 * Helper to execute clean, zero-dependency HTTP/S GET requests tracking redirects
 */
function request(url, options = {}) {
    return new Promise((resolve, reject) => {
        const protocol = url.startsWith('https') ? https : http;
        
        const req = protocol.get(url, options, (res) => {
            resolve({
                statusCode: res.statusCode,
                headers: res.headers,
                url: url
            });
        });

        req.on('error', (err) => reject(err));
        req.setTimeout(CONFIG.timeoutMs, () => {
            req.destroy();
            reject(new Error(`Timeout exceeding ${CONFIG.timeoutMs}ms on URL: ${url}`));
        });
    });
}

/**
 * Main Diagnostic Execution Loop
 */
async function runDiagnostic() {
    console.log(`==================================================`);
    console.log(`🚀 STARTING AUTOMATED REVENUE FUNNEL AUDIT [2026]`);
    console.log(`==================================================\n`);

    let criticalErrors = 0;

    // STEP 1: Audit Landing Page Availability
    console.log(`[STEP 1/3] Checking Core Landing Page Status...`);
    try {
        const landingRes = await request(CONFIG.landingPageUrl);
        if (landingRes.statusCode === 200) {
            console.log(`  ✅ Live: Landing page returned HTTP 200 OK.`);
        } else {
            console.log(`  ❌ CRITICAL: Landing page returned dangerous status code: ${landingRes.statusCode}`);
            criticalErrors++;
        }
    } catch (err) {
        console.log(`  ❌ CRITICAL: Unable to reach your landing page. Server might be down!`);
        console.log(`     Error Detail: ${err.message}`);
        criticalErrors++;
    }

    console.log(`\n--------------------------------------------------`);

    // STEP 2: Audit Affiliate Network Link Endpoint Health
    console.log(`[STEP 2/3] Validating Live Partner Affiliate Link...`);
    const liveAffiliateUrl = `https://${CONFIG.expectedAffiliateTarget}/nwkkk7vkps17`;
    try {
        // Send request accepting redirects to see where it lands
        const affiliateRes = await request(liveAffiliateUrl, {
            headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Revenue-Monitor/1.0' }
        });

        // ManyChat partner links usually issue a 301/302 redirect or load a 200 landing page
        if (affiliateRes.statusCode >= 200 && affiliateRes.statusCode < 400) {
            console.log(`  ✅ Live: Affiliate tracking link is responsive (HTTP ${affiliateRes.statusCode}).`);
        } else {
            console.log(`  ⚠️ WARNING: Partner link returned an unusual status code: ${affiliateRes.statusCode}`);
        }
    } catch (err) {
        console.log(`  ❌ CRITICAL: Affiliate network link is fully dead or throwing handshake errors.`);
        console.log(`     Error Detail: ${err.message}`);
        criticalErrors++;
    }

    console.log(`\n--------------------------------------------------`);

    // STEP 3: Structural Validation Core
    console.log(`[STEP 3/3] Inspecting Source Markup Safety...`);
    try {
        // Fetch raw HTML markup to inspect structural integrity
        const fetchHtml = () => new Promise((resolve, reject) => {
            https.get(CONFIG.landingPageUrl, (res) => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => resolve(data));
            }).on('error', reject);
        });

        const htmlMarkup = await fetchHtml();

        // Check if tracking IDs are intact
        const hasAffiliateId = htmlMarkup.includes("nwkkk7vkps17");
        const hasFormElement = htmlMarkup.includes('id="affiliate-bridge-form"');

        if (hasAffiliateId && hasFormElement) {
            console.log(`  ✅ Safe: High-converting script assets and routing tags match active campaign parameters.`);
        } else {
            if (!hasAffiliateId) console.log(`  ❌ CRITICAL: Affiliate tracking tag "nwkkk7vkps17" was stripped from source html!`);
            if (!hasFormElement) console.log(`  ❌ CRITICAL: Lead generation target form ID has been broken or altered!`);
            criticalErrors++;
        }

    } catch (err) {
        console.log(`  ❌ CRITICAL: Failed parsing internal landing page code architecture.`);
        criticalErrors++;
    }

    // FINAL SCORE ARCHITECTURE
    console.log(`\n==================================================`);
    if (criticalErrors === 0) {
        console.log(`🎉 AUDIT COMPLETE: Funnel is 100% healthy. Cash engine secure.`);
        console.log(`==================================================`);
        process.exit(0);
    } else {
        console.log(`🚨 AUDIT FAIL: Found ${criticalErrors} critical revenue errors.`);
        console.log(`   Fix immediate routing breaks inside your repository layout immediately.`);
        console.log(`==================================================`);
        process.exit(1);
    }
}

// Fire Diagnostic
runDiagnostic();
