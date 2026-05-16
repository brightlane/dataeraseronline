import os

# Define your low-competition target niches
niches = [
    {
        "slug": "real-estate-agents",
        "keyword": "Independent Real Estate Agents",
        "industry": "Real Estate",
        "trigger_word": "LISTING",
        "asset": "Property PDF walkthrough and price-range screener"
    },
    {
        "slug": "commercial-roofing",
        "keyword": "Commercial Roofing Contractors",
        "industry": "Roofing & Construction",
        "trigger_word": "ESTIMATE",
        "asset": "Roofing Lead Qualifier & Quote Estimator Blueprint"
    },
    {
        "slug": "boutique-bridal",
        "keyword": "Boutique Bridal Dress Shops",
        "industry": "Retail & Bridal",
        "trigger_word": "BRIDAL",
        "asset": "Fitting Appointment Booking & Dress Catalog Automation"
    },
    {
        "slug": "structural-engineers",
        "keyword": "Structural Engineering Firms",
        "industry": "Professional Services",
        "trigger_word": "BLUEPRINT",
        "asset": "B2B Project Consult Intake Flow"
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ManyChat {keyword} Blueprint: Automate Leads 24/7</title>
    <meta name="description" content="Download the exact ManyChat automated lead funnel template built specifically for {keyword}. Capture high-intent clients on autopilot.">
    <link rel="canonical" href="https://manychat.partnerlinks.io/nwkkk7vkps17">
    
    <style>
        :root {{
            --primary: #1E3A8A;
            --accent: #10B981;
            --bg: #F3F4F6;
            --text: #1F2937;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 2rem 20px; }}
        
        .card {{ background: white; padding: 2.5rem; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 2rem; }}
        h1 {{ color: var(--primary); font-size: 2.2rem; line-height: 1.2; margin-bottom: 1rem; }}
        h2 {{ color: var(--primary); font-size: 1.5rem; margin-top: 2rem; margin-bottom: 1rem; }}
        
        .step-list {{ margin: 1.5rem 0; padding-left: 1.5rem; }}
        .step-list li {{ margin-bottom: 1rem; }}
        
        .highlight-box {{ background: #EFF6FF; border-left: 4px solid var(--primary); padding: 1.5rem; border-radius: 0 12px 12px 0; margin: 2rem 0; }}
        
        .bridge-container {{ background: linear-gradient(135deg, var(--primary), #3B82F6); color: white; padding: 2.5rem; border-radius: 12px; text-align: center; margin-top: 3rem; }}
        .bridge-container h3 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
        .bridge-form {{ display: flex; max-width: 500px; margin: 1.5rem auto 0; gap: 0; border-radius: 50px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
        .bridge-form input {{ flex: 1; padding: 1rem 1.5rem; border: none; outline: none; font-size: 1rem; color: #111827; }}
        .bridge-form button {{ background: var(--accent); color: white; padding: 1rem 2rem; border: none; font-weight: 700; cursor: pointer; font-size: 1rem; transition: background 0.2s; }}
        .bridge-form button:hover {{ background: #059669; }}
        
        .footer-text {{ text-align: center; font-size: 0.85rem; color: #6B7280; margin-top: 3rem; }}
        
        @media (max-width: 600px) {{
            .bridge-form {{ flex-direction: column; border-radius: 12px; gap: 10px; box-shadow: none; background: transparent; }}
            .bridge-form input, .bridge-form button {{ border-radius: 8px; width: 100%; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <article class="card">
        <h1>How to Set Up a ManyChat {industry} Lead Funnel (Zero Coding Required)</h1>
        <p>If you are operating within {keyword}, spending your valuable hours manually checking messages and qualifying raw inquiries wastes operational revenue. This architectural blueprint establishes a native, 24/7 screening mechanism inside social chat ecosystems.</p>
        
        <div class="highlight-box">
            <strong>The Automated Strategy:</strong> When a prospective customer comments the high-intent trigger phrase <strong>"{trigger_word}"</strong> on your targeted visual media channels, ManyChat automatically initiates an immediate sequence, delivering a {asset} straight to their inbound feed while capturing verified business data.
        </div>

        <h2>Step 1: Configure the Keyword Ingestion Gateway</h2>
        <p>Inside your communication engine workspace, instantiate a fresh automation canvas. Connect a new trigger listening exclusively for <strong>"User Comments on Your Post or Reel"</strong>. Restrict the criteria filter strictly to the exact value string matching your campaign: <em>{trigger_word}</em>.</p>

        <h2>Step 2: Map the Qualification & Conditional Sequence</h2>
        <ul class="step-list">
            <li><strong>Interactive Touchpoint 1:</strong> Fire a low-friction diagnostic query evaluating the prospect's project timeline or purchase urgency.</li>
            <li><strong>Interactive Touchpoint 2:</strong> Programmatically lock data attributes into custom storage fields using native user input validation blocks.</li>
        </ul>

        <h2>Step 3: Deploy the Production Blueprint Directly</h2>
        <p>Skip the initial logic setup from scratch. You can import our verified structural recipe block config directly into your specific workspace profile instantly.</p>

        <div class="bridge-container">
            <h3>Download the {industry} Blueprint Pack</h3>
            <p>Input your operational tracking mail below to receive your 1-click execution link. Completely compatible with all ManyChat tiers.</p>
            <form class="bridge-form" id="lead-capture-bridge">
                <input type="email" placeholder="Enter your business email" required>
                <button type="submit">Get Blueprint Links</button>
            </form>
        </div>
    </article>

    <p class="footer-text">
        Disclaimer: This architecture functions as a deployment implementation guide. We receive affiliate compensation if you opt to scale to premium plans through our execution hooks.
    </p>
</div>

<script>
    document.getElementById('lead-capture-bridge').addEventListener('submit', function(e) {{
        e.preventDefault();
        window.location.href = "https://manychat.partnerlinks.io/nwkkk7vkps17";
    }});
</script>

</body>
</html>
"""

# Execute build cycle
def build_engine():
    generated_count = 0
    for item in niches:
        filename = f"{item['slug']}.html"
        output_data = html_template.format(
            keyword=item['keyword'],
            industry=item['industry'],
            trigger_word=item['trigger_word'],
            asset=item['asset']
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output_data)
        print(f"✅ Generated: {filename}")
        generated_count += 1
    print(f"--- Build complete. Total high-velocity pages outputted: {generated_count} ---")

if __name__ == "__main__":
    build_engine()
