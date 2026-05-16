/**
 * Automated Programmatic Funnel Factory Engine
 * Target: Generates responsive static HTML landers matching exact affiliate IDs.
 * Run Command: node build-funnels.js
 */

const fs = require('fs');
const path = require('path');

// Core Database Array for programmatic creation
const CAMPAIGNS = [
    {
        folder: "ManyChat",
        title: "Scale Instagram DMs to $10k/mo on Autopilot",
        subheading: "Stop letting hot leads die in your requests. Deploy high-converting message paths in 5 minutes.",
        affiliateUrl: "https://manychat.partnerlinks.io/nwkkk7vkps17",
        formId: "manychat-bridge-form",
        ctaText: "Claim Your 14-Day Free Trial",
        badgeColor: "#0084FF"
    }
];

/**
 * Returns raw, zero-dependency, ultra-fast structural layout string
 */
function getHtmlTemplate(data) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${data.title} | Global Automation Hub</title>
    <style>
        :root { --brand-color: ${data.badgeColor}; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: #0b0f19; color: #f3f4f6; display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 20px; }
        .card { background: #111827; border: 1px solid #1f2937; border-radius: 12px; max-width: 540px; width: 100%; padding: 40px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3); }
        .badge { display: inline-block; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--brand-color); padding: 6px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.05em; }
        h1 { font-size: 2.2rem; font-weight: 800; line-height: 1.2; color: #ffffff; margin-bottom: 16px; }
        p { color: #9ca3af; font-size: 1.05rem; line-height: 1.6; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; position: relative; }
        input[type="email"] { width: 100%; background: #1f2937; border: 2px solid #374151; padding: 16px; border-radius: 8px; color: #fff; font-size: 1rem; outline: none; transition: border-color 0.2s; }
        input[type="email"]:focus { border-color: var(--brand-color); }
        button { width: 100%; background: var(--brand-color); color: #ffffff; border: none; padding: 16px; border-radius: 8px; font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: transform 0.1s, filter 0.2s; }
        button:hover { filter: brightness(1.1); }
        button:active { transform: scale(0.98); }
        footer { margin-top: 25px; text-align: center; font-size: 0.8rem; color: #4b5563; }
        footer a { color: #6b7280; text-decoration: none; }
    </style>
</head>
<body>

    <div class="card">
        <div class="badge">Official Partner Integration</div>
        <h1>${data.title}</h1>
        <p>${data.subheading}</p>

        <form id="${data.formId}" onsubmit="handleLeadCapture(event)">
            <div class="form-group">
                <input type="email" id="user-email" placeholder="Enter your business email..." required />
            </div>
            <button type="submit">${data.ctaText} &rarr;</button>
        </form>

        <footer>
            Secure connection verified. <a href="#">Terms of Service</a>
        </footer>
    </div>

    <script>
        function handleLeadCapture(event) {
            event.preventDefault();
            const emailValue = document.getElementById('user-email').value;
            
            // Fast asynchronous exit-intent execution
            console.log("Captured lead routing:", emailValue);
            
            // Hard instantaneous redirection to target conversion link
            window.location.href = "${data.affiliateUrl}";
        }
    </script>
</body>
</html>`;
}

/**
 * Iterates through campaigns and safely outputs structural folders
 */
function buildOutputDirectories() {
    console.log(`==================================================`);
    console.log(`🏗️  RUNNING HIGH-VELOCITY REPOSITORY BUILDER`);
    console.log(`==================================================\n`);

    CAMPAIGNS.forEach((campaign) => {
        const targetDir = path.join(__dirname, campaign.folder);
        
        // Ensure destination folder exists safely
        if (!fs.existsSync(targetDir)){
            fs.mkdirSync(targetDir, { recursive: true });
            console.log(`[DIR CREATED] Outbound path created: /${campaign.folder}`);
        }

        const htmlContent = getHtmlTemplate(campaign);
        const targetFilePath = path.join(targetDir, 'index.html');

        // Output raw minified structural file asset
        fs.writeFileSync(targetFilePath, htmlContent, 'utf-8');
        console.log(`  ✅ [FILE DEPLOYED] Successfully generated: /${campaign.folder}/index.html`);
    });

    console.log(`\n==================================================`);
    console.log(`🎉 BUILD SPRINT COMPLETE: Campaigns structuralized.`);
    console.log(`==================================================`);
}

buildOutputDirectories();
