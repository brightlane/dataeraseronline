/**
 * Programmatic Long-Tail Matrix Generator
 * Target: Automates generation of highly optimized variant landing pages
 * Run Command: node generate-matrix.js
 */

const fs = require('fs');
const path = require('path');

// Target High-Intent Search Matrix for 2026
const MATRIX_PAGES = [
    {
        filename: "manychat-pricing-guide.html",
        title: "ManyChat Pricing Guide 2026: Hidden Costs & Free vs Pro Plans",
        h1: "Is ManyChat Pro Worth It? 2026 Cost Breakdown",
        intro: "Don't overpay for your automation stack. Discover exactly what features are locked behind the Pro paywall and how subscriber tiers affect your monthly bill.",
        metaDesc: "Comprehensive breakdown of ManyChat pricing structures, platform fees, and subscriber tiers for 2026."
    },
    {
        filename: "manychat-vs-chatfuel-comparison.html",
        title: "ManyChat vs Chatfuel: Which Instagram Bot Wins in 2026?",
        h1: "ManyChat vs Chatfuel: The Ultimate 2026 Showdown",
        intro: "Choosing the wrong DM automation platform can break your workflows. We compare UI simplicity, AI integration capabilities, and API reliability head-to-head.",
        metaDesc: "An un-biased, deep-dive comparison between ManyChat and Chatfuel for modern marketing automation."
    },
    {
        filename: "best-instagram-automation-tools.html",
        title: "5 Best Instagram Automation Tools for High-Velocity Lead Gen",
        h1: "Top Instagram DM Automation Platforms Evaluated",
        intro: "Scaling your brand requires hands-off chat infrastructure. Explore the top-rated official Meta partner applications designed to convert story replies into revenue.",
        metaDesc: "Discover the leading Instagram automation engines tested for conversion velocity, delivery tracking, and compliance."
    }
];

const TRACKING_ID = "nwkkk7vkps17";
const COMP_URL = `https://manychat.partnerlinks.io/${TRACKING_ID}`;

function buildTemplate(page) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="${page.metaDesc}">
    <title>${page.title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root { --bg: #090d16; --card: #111827; --text: #f3f4f6; --accent: #3b82f6; --border: #1f2937; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background-color: var(--bg); color: var(--text); padding: 2rem 1rem; }
        .container { max-width: 800px; margin: 4rem auto; background: var(--card); border: 1px solid var(--border); padding: 3rem 2rem; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
        .badge { display: inline-block; background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.2); color: var(--accent); padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 1.5rem; }
        h1 { font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 1.5rem; letter-spacing: -0.02em; color: #fff; }
        p.intro { font-size: 1.15rem; color: #9ca3af; line-height: 1.7; margin-bottom: 2.5rem; }
        
        .optin-box { background: #1f2937; border: 1px solid #374151; padding: 2rem; border-radius: 8px; margin-top: 2rem; }
        .optin-box h3 { font-size: 1.3rem; margin-bottom: 0.75rem; color: #fff; }
        .optin-box p { color: #9ca3af; font-size: 0.95rem; margin-bottom: 1.5rem; }
        
        .form-group { display: flex; gap: 10px; }
        input[type="email"] { flex: 1; background: #111827; border: 2px solid #374151; padding: 1rem; border-radius: 6px; color: #fff; font-size: 1rem; outline: none; }
        input[type="email"]:focus { border-color: var(--accent); }
        button { background: var(--accent); color: #fff; border: none; padding: 1rem 2rem; font-size: 1rem; font-weight: 700; border-radius: 6px; cursor: pointer; transition: opacity 0.2s; }
        button:hover { opacity: 0.9; }
        
        footer { margin-top: 4rem; text-align: center; font-size: 0.85rem; color: #4b5563; border-top: 1px solid var(--border); padding-top: 1.5rem; }
    </style>
</head>
<body>

    <div class="container">
        <div class="badge">In-Depth Analysis</div>
        <h1>${page.h1}</h1>
        <p class="intro">${page.intro}</p>

        <div class="optin-box">
            <h3>⚡ Access Premium Pre-Built Conversion Blueprints</h3>
            <p>Deploy our top 10 verified automation templates instantly to jumpstart your customer acquisition funnel.</p>
            
            <form id="affiliate-bridge-form" onsubmit="executeRoute(event)">
                <div class="form-group">
                    <input type="email" id="lead-email" placeholder="Enter your best professional email..." required />
                    <button type="submit">Get Blueprints &rarr;</button>
                </div>
            </form>
        </div>

        <footer>
            © 2026 ChatBotProReviews. Verified Meta Developer Partner Ecosystem.
        </footer>
    </div>

    <script>
        function executeRoute(e) {
            e.preventDefault();
            const email = document.getElementById('lead-email').value;
            console.log("Saving lead...", email);
            
            // Immediate pass-through to secure affiliate destination link
            window.location.href = "${COMP_URL}";
        }
    </script>
</body>
</html>`;
}

function generateMatrix() {
    console.log(`==================================================`);
    console.log(`🏗️  LAUNCHING PROGRAMMATIC MATRIX DEPLOYMENT`);
    console.log(`==================================================\n`);

    MATRIX_PAGES.forEach((page) => {
        const targetPath = path.join(__dirname, page.filename);
        const htmlMarkup = buildTemplate(page);
        
        fs.writeFileSync(targetPath, htmlMarkup, 'utf-8');
        console.log(`  ✅ [DEPLOYED] Generated: /${page.filename}`);
    });

    console.log(`\n==================================================`);
    console.log(`🎉 MATRIX MATRIX COMPILED: Ready for indexing.`);
    console.log(`==================================================`);
}

generateMatrix();
