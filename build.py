#!/usr/bin/env python3
"""
Wondershare Dr.Fone — Data Eraser SEO Site Builder v2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Domain : brightlane.github.io/dataeraseronline
Keywords: 250+ (was 150)
Blogs   : 15 expanded posts
Cats    : 15 (adds pc-file-erase, broken-phone, business-compliance)
Theme   : dark crimson #dc2626 on deep charcoal #0f172a
Hook    : "Factory Reset Is Not Enough"

python3 build.py  →  ./dist/
"""

import os, json, sys
from datetime import date
from collections import defaultdict
from pathlib import Path

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949104659004532&atid=dataeraserwebs"
SITE_DOMAIN   = "https://brightlane.github.io/dataeraseronline"
BASE_PATH     = "/dataeraseronline"
BUILD_DATE    = date.today().isoformat()
DIST          = Path("dist")
YEAR          = date.today().year

# ═══════════════════════════════════════════════════════════════
#  KEYWORDS — 250+
# ═══════════════════════════════════════════════════════════════
KEYWORDS = []
_seen = set()

def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# ── brand ──────────────────────────────────────────────────────
for s, k in [
    ("wondershare-data-eraser",           "Wondershare Data Eraser"),
    ("drfone-data-eraser",                "Dr.Fone Data Eraser"),
    ("drfone-data-eraser-review",         "Dr.Fone Data Eraser review 2025"),
    ("drfone-data-eraser-review-honest",  "Dr.Fone Data Eraser honest review"),
    ("drfone-data-eraser-download",       "Dr.Fone Data Eraser download"),
    ("drfone-data-eraser-free",           "Dr.Fone Data Eraser free trial"),
    ("drfone-data-eraser-price",          "Dr.Fone Data Eraser price 2025"),
    ("drfone-data-eraser-safe",           "is Dr.Fone Data Eraser safe"),
    ("drfone-data-eraser-legit",          "is Dr.Fone Data Eraser legit"),
    ("drfone-data-eraser-worth-it",       "Dr.Fone Data Eraser worth it 2025"),
    ("drfone-data-eraser-features",       "Dr.Fone Data Eraser features list"),
    ("drfone-data-eraser-tutorial",       "Dr.Fone Data Eraser tutorial"),
    ("drfone-data-eraser-windows",        "Dr.Fone Data Eraser Windows"),
    ("drfone-data-eraser-mac",            "Dr.Fone Data Eraser Mac"),
    ("drfone-data-eraser-android",        "Dr.Fone Data Eraser Android"),
    ("drfone-data-eraser-iphone",         "Dr.Fone Data Eraser iPhone iOS"),
    ("drfone-data-eraser-alternative",    "Dr.Fone Data Eraser alternatives"),
    ("drfone-data-eraser-coupon",         "Dr.Fone Data Eraser coupon 2025"),
    ("drfone-data-eraser-discount",       "Dr.Fone Data Eraser discount 2025"),
    ("drfone-data-eraser-lifetime",       "Dr.Fone Data Eraser lifetime license"),
]:
    kw(s, k, "brand")

# ── erase-before-selling ───────────────────────────────────────
for s, k in [
    ("erase-phone-before-selling",        "erase phone before selling"),
    ("wipe-phone-before-selling",         "wipe phone before selling"),
    ("factory-reset-not-enough",          "factory reset is not enough"),
    ("data-remains-after-factory-reset",  "data remains after factory reset"),
    ("sell-old-phone-safely",             "sell old phone safely"),
    ("sell-iphone-safely",                "how to sell iPhone safely"),
    ("sell-android-safely",               "how to sell Android phone safely"),
    ("delete-data-before-trade-in",       "delete data before phone trade in"),
    ("erase-phone-before-trade-in",       "erase phone before trade in"),
    ("phone-trade-in-data-security",      "phone trade in data security"),
    ("wipe-samsung-before-selling",       "wipe Samsung before selling"),
    ("wipe-pixel-before-selling",         "wipe Google Pixel before selling"),
    ("erase-oneplus-before-selling",      "erase OnePlus before selling"),
    ("give-away-old-phone-safely",        "give away old phone safely"),
    ("recycle-phone-data-security",       "recycle phone data security"),
    ("donate-old-phone-safely",           "donate old phone safely"),
    ("erase-refurbished-phone",           "how to erase refurbished phone"),
]:
    kw(s, k, "erase-before-selling")

# ── privacy-protection ─────────────────────────────────────────
for s, k in [
    ("permanent-data-deletion",           "permanent data deletion phone"),
    ("how-to-permanently-delete-data",    "how to permanently delete data from phone"),
    ("data-recovery-after-factory-reset", "data recovery after factory reset possible"),
    ("overwrite-phone-data",              "overwrite phone data securely"),
    ("dod-5220-22-m-phone",               "DoD 5220.22-M phone erasure"),
    ("military-grade-data-wipe",          "military grade data wipe mobile"),
    ("phone-privacy-protection",          "phone privacy protection data wipe"),
    ("stop-data-recovery-phone",          "stop data recovery from old phone"),
    ("identity-theft-old-phone",          "identity theft risk old phone"),
    ("protect-personal-data-phone",       "protect personal data on old phone"),
    ("nist-800-88-mobile",                "NIST 800-88 mobile device erasure"),
    ("secure-data-wipe-standards",        "secure data wipe standards mobile"),
    ("prevent-data-breach-phone",         "prevent data breach old phone"),
    ("biometric-data-erase-phone",        "erase biometric data from phone"),
]:
    kw(s, k, "privacy-protection")

# ── iphone-erase ──────────────────────────────────────────────
for s, k in [
    ("erase-iphone-permanently",          "erase iPhone permanently"),
    ("wipe-iphone-securely",              "wipe iPhone securely"),
    ("iphone-data-eraser",                "iPhone data eraser software"),
    ("ios-data-eraser",                   "iOS data eraser tool"),
    ("erase-iphone-without-icloud",       "erase iPhone without iCloud"),
    ("selective-erase-iphone",            "selective erase iPhone without factory reset"),
    ("delete-photos-iphone-permanently",  "delete photos iPhone permanently"),
    ("delete-contacts-iphone-permanently","delete contacts iPhone permanently"),
    ("erase-messages-iphone-permanently", "erase messages iPhone permanently"),
    ("iphone-15-data-erase",              "iPhone 15 data erase before selling"),
    ("iphone-14-data-erase",              "iPhone 14 secure erase"),
    ("iphone-13-erase",                   "iPhone 13 erase permanently"),
    ("erase-ipad-before-selling",         "erase iPad before selling"),
    ("wipe-apple-watch-data",             "wipe Apple Watch data securely"),
    ("erase-ios-17-phone",                "erase iOS 17 phone data"),
    ("iphone-jailbreak-data-erase",       "erase jailbroken iPhone data"),
    ("erase-iphone-se",                   "erase iPhone SE permanently"),
]:
    kw(s, k, "iphone-erase")

# ── android-erase ─────────────────────────────────────────────
for s, k in [
    ("erase-android-permanently",         "erase Android phone permanently"),
    ("wipe-android-securely",             "wipe Android securely before selling"),
    ("android-data-eraser",               "Android data eraser software"),
    ("erase-samsung-permanently",         "erase Samsung Galaxy permanently"),
    ("samsung-factory-reset-not-safe",    "Samsung factory reset not safe"),
    ("samsung-data-recovery-risk",        "Samsung data recovery risk after reset"),
    ("erase-google-pixel",                "erase Google Pixel securely"),
    ("erase-xiaomi-permanently",          "erase Xiaomi phone permanently"),
    ("erase-huawei-permanently",          "erase Huawei permanently"),
    ("erase-oppo-permanently",            "erase OPPO phone permanently"),
    ("erase-vivo-phone",                  "erase Vivo phone permanently"),
    ("erase-motorola-permanently",        "erase Motorola phone permanently"),
    ("erase-lg-phone",                    "erase LG phone permanently"),
    ("android-selective-erase",           "Android selective erase app"),
    ("android-14-data-erase",             "Android 14 secure data erase"),
    ("android-13-erase",                  "Android 13 data erase permanently"),
    ("erase-android-tablet",              "erase Android tablet permanently"),
]:
    kw(s, k, "android-erase")

# ── junk-cleanup ──────────────────────────────────────────────
for s, k in [
    ("clean-junk-files-phone",            "clean junk files from phone"),
    ("free-up-storage-phone",             "free up storage on phone fast"),
    ("delete-cache-phone",                "delete cache on phone permanently"),
    ("remove-temp-files-phone",           "remove temp files from phone"),
    ("phone-storage-cleaner",             "phone storage cleaner software"),
    ("delete-large-files-phone",          "find and delete large files phone"),
    ("clean-iphone-storage",              "clean iPhone storage junk files"),
    ("clean-android-storage",             "clean Android storage junk"),
    ("photo-compressor-phone",            "photo compressor phone storage"),
    ("delete-duplicate-photos-phone",     "delete duplicate photos phone"),
    ("clear-app-data-phone",              "clear app data phone permanently"),
]:
    kw(s, k, "junk-cleanup")

# ── erasure-report ────────────────────────────────────────────
for s, k in [
    ("data-erasure-report",               "data erasure report certificate"),
    ("erasure-certificate-phone",         "erasure certificate phone"),
    ("proof-of-data-deletion",            "proof of data deletion phone"),
    ("erasure-report-resale-value",       "erasure report increases resale value"),
    ("gdpr-erasure-report",               "GDPR data erasure report phone"),
    ("hipaa-erasure-certificate",         "HIPAA erasure certificate mobile"),
    ("erasure-report-pdf",                "data erasure report PDF download"),
    ("certified-data-wipe-report",        "certified data wipe report"),
]:
    kw(s, k, "erasure-report")

# ── compare ───────────────────────────────────────────────────
for s, k in [
    ("best-data-eraser-software-2025",    "best data eraser software 2025"),
    ("drfone-vs-iskysoft-eraser",         "Dr.Fone vs iSkysoft data eraser"),
    ("drfone-vs-imobie-eraser",           "Dr.Fone vs iMobie PhoneClean"),
    ("drfone-vs-decipher-backup",         "Dr.Fone vs Decipher backup"),
    ("best-iphone-data-eraser",           "best iPhone data eraser 2025"),
    ("best-android-data-eraser",          "best Android data eraser 2025"),
    ("free-vs-paid-data-eraser",          "free vs paid data eraser software"),
    ("data-eraser-vs-factory-reset",      "data eraser software vs factory reset"),
    ("eraser-software-comparison-2025",   "data eraser software comparison 2025"),
    ("top-rated-phone-eraser",            "top rated phone eraser tools 2025"),
]:
    kw(s, k, "compare")

# ── howto ─────────────────────────────────────────────────────
for s, k in [
    ("how-to-permanently-erase-iphone",   "how to permanently erase iPhone data"),
    ("how-to-permanently-erase-android",  "how to permanently erase Android data"),
    ("how-to-wipe-phone-before-selling",  "how to wipe phone before selling step by step"),
    ("how-to-check-if-data-erased",       "how to check if phone data is really erased"),
    ("how-to-erase-without-computer",     "how to erase phone data without computer"),
    ("how-to-get-erasure-report",         "how to get a data erasure report"),
    ("how-to-erase-specific-files-only",  "how to erase specific files only phone"),
    ("how-to-erase-before-repair",        "how to erase phone before repair shop"),
    ("how-to-verify-data-gone",           "how to verify phone data is gone"),
]:
    kw(s, k, "howto")

# ── platform ──────────────────────────────────────────────────
for s, k in [
    ("data-eraser-windows-11",            "data eraser software Windows 11"),
    ("data-eraser-windows-10",            "data eraser software Windows 10"),
    ("data-eraser-macos-ventura",         "data eraser macOS Ventura"),
    ("data-eraser-macos-sonoma",          "data eraser macOS Sonoma 2025"),
    ("iphone-eraser-mac",                 "iPhone eraser for Mac"),
    ("android-eraser-windows",            "Android eraser for Windows PC"),
]:
    kw(s, k, "platform")

# ── global ────────────────────────────────────────────────────
for s, k in [
    ("data-eraser-uk",                    "data eraser software UK 2025"),
    ("data-eraser-canada",                "data eraser Canada"),
    ("data-eraser-australia",             "data eraser Australia"),
    ("data-eraser-germany",               "Datenlöscher Software Deutschland"),
    ("data-eraser-france",                "effacer données téléphone logiciel"),
    ("data-eraser-japan",                 "データ消去 スマホ ソフト"),
    ("data-eraser-india",                 "data eraser India mobile 2025"),
    ("data-eraser-brazil",                "apagar dados celular software"),
    ("data-eraser-singapore",             "data eraser Singapore phone"),
    ("data-eraser-uae",                   "data eraser UAE phone"),
]:
    kw(s, k, "global")

# ── usecase ───────────────────────────────────────────────────
for s, k in [
    ("erase-phone-after-divorce",         "erase phone data after divorce"),
    ("erase-company-phone",               "erase company phone before returning"),
    ("erase-phone-before-customs",        "erase phone before crossing border customs"),
    ("erase-phone-theft-prevention",      "erase phone data theft prevention"),
    ("erase-phone-before-repair",         "erase phone data before repair"),
    ("erase-phone-lost-stolen",           "erase data lost or stolen phone"),
    ("erase-ex-partner-data",             "remove ex partner data from phone"),
    ("erase-medical-data-phone",          "erase medical data from phone"),
    ("erase-banking-data-phone",          "erase banking data from old phone"),
    ("erase-business-data-phone",         "erase business data from personal phone"),
]:
    kw(s, k, "usecase")

# ── pc-file-erase (NEW) ───────────────────────────────────────
for s, k in [
    ("permanently-delete-files-windows",  "permanently delete files Windows 10 11"),
    ("shred-files-pc",                    "shred files permanently PC"),
    ("overwrite-deleted-files-windows",   "overwrite deleted files Windows"),
    ("permanently-delete-files-mac",      "permanently delete files Mac"),
    ("wipe-free-space-windows",           "wipe free space Windows securely"),
    ("secure-file-deletion-tool",         "secure file deletion tool Windows Mac"),
    ("delete-files-beyond-recovery",      "delete files beyond recovery PC"),
    ("erase-ssd-data-permanently",        "erase SSD data permanently"),
    ("erase-hard-drive-before-selling",   "erase hard drive before selling PC"),
    ("wipe-laptop-before-selling",        "wipe laptop before selling data"),
    ("secure-delete-windows-11",          "secure delete Windows 11 free"),
    ("permanently-delete-photos-pc",      "permanently delete photos from PC"),
]:
    kw(s, k, "pc-file-erase")

# ── broken-phone (NEW) ────────────────────────────────────────
for s, k in [
    ("erase-broken-phone-data",           "erase data from broken phone"),
    ("wipe-cracked-screen-phone",         "wipe phone with cracked screen"),
    ("erase-water-damaged-phone",         "erase water damaged phone data"),
    ("erase-phone-wont-turn-on",          "erase phone that wont turn on"),
    ("secure-erase-dead-phone",           "secure erase dead phone"),
    ("erase-phone-before-recycle-broken", "erase broken phone before recycling"),
    ("recover-erase-broken-iphone",       "erase broken iPhone data"),
    ("erase-broken-android",              "erase broken Android phone data"),
    ("wipe-phone-black-screen",           "wipe phone stuck on black screen"),
]:
    kw(s, k, "broken-phone")

# ── business-compliance (NEW) ─────────────────────────────────
for s, k in [
    ("gdpr-mobile-data-erasure",          "GDPR mobile device data erasure"),
    ("hipaa-phone-data-wipe",             "HIPAA compliant phone data wipe"),
    ("corporate-phone-erasure-policy",    "corporate phone erasure policy"),
    ("it-department-phone-wipe",          "IT department phone wipe procedure"),
    ("enterprise-data-erasure-solution",  "enterprise data erasure solution"),
    ("mdm-phone-wipe-vs-data-eraser",     "MDM phone wipe vs data eraser software"),
    ("pci-dss-mobile-device-wipe",        "PCI DSS mobile device data wipe"),
    ("iso-27001-phone-disposal",          "ISO 27001 phone disposal procedure"),
    ("byod-data-erasure-policy",          "BYOD data erasure policy"),
    ("employee-offboarding-phone-wipe",   "employee offboarding phone wipe"),
    ("nist-800-88-mobile-device",         "NIST 800-88 mobile device sanitization"),
    ("decommission-company-phones",       "decommission company phones securely"),
    ("bulk-phone-erasure-business",       "bulk phone erasure business software"),
]:
    kw(s, k, "business-compliance")

print(f"Keywords loaded: {len(KEYWORDS)}")

# ═══════════════════════════════════════════════════════════════
#  BLOG POSTS — 15 expanded
# ═══════════════════════════════════════════════════════════════
BLOG_POSTS = [
    {
        "slug": "factory-reset-not-enough-research",
        "title": "Factory Reset Is Not Enough: What Research Really Shows",
        "date": "2025-06-01",
        "desc": "Cambridge University researchers recovered data from factory-reset Android phones. Here's what that means for you — and how to fix it.",
        "content": """<p>In 2015, researchers from Cambridge University bought 20 second-hand Android phones and attempted to recover data from devices that had been factory reset. They successfully recovered photos, emails, text messages, contacts, and Google authentication tokens from the majority of devices — even those that appeared to have been wiped completely.</p>
<p>The core problem: factory reset does not overwrite your data. It removes the file allocation table — the index that tells the OS where files live — but the actual data blocks remain on the flash storage until overwritten by new data. With the right recovery software (freely available), anyone can reconstruct those files.</p>
<h2>Why This Matters More in 2025</h2>
<p>Flash storage (NAND) has become denser and more sophisticated. Modern iPhones use hardware encryption, but Android implementations vary wildly by manufacturer. Many budget Android devices do not enable full-disk encryption by default, making factory-reset data recovery trivial.</p>
<p>Even on encrypted devices, if the encryption keys are not properly destroyed during a factory reset, decryption remains possible.</p>
<h2>What Proper Erasure Looks Like</h2>
<p>True data sanitization requires either overwriting every storage cell with pseudorandom data (the DoD 5220.22-M method) or cryptographic erasure — where the encryption key is destroyed and the storage is then overwritten. Dr.Fone Data Eraser does both: it overwrites data using military-grade algorithms, then generates a PDF erasure certificate with a timestamp and your device's IMEI number.</p>
<p>Bottom line: factory reset protects you from casual snooping. It does not protect you from anyone with $50 of data recovery software and 30 minutes.</p>"""
    },
    {
        "slug": "erase-iphone-before-selling-2025",
        "title": "How to Erase iPhone Before Selling — 2025 Complete Guide",
        "date": "2025-06-05",
        "desc": "Apple's built-in erase leaves recoverable data. Here's the right way to permanently wipe your iPhone before selling, trading in, or giving it away.",
        "content": """<p>Apple's "Erase All Content and Settings" function is convenient, but it's not the same as permanent data destruction. The process removes your iCloud account and triggers a factory reset — but the underlying data on the NAND storage may remain recoverable.</p>
<h2>The Problem with Apple's Default Erase</h2>
<p>Since iPhone 3GS, Apple has used hardware encryption. When you erase, the device discards the encryption key, making existing data theoretically inaccessible. However, forensic tools used by law enforcement — and increasingly available commercially — can sometimes extract data by exploiting vulnerabilities in the secure enclave or bootloader chain.</p>
<p>For maximum security before selling, you should go further than Apple's built-in option.</p>
<h2>Step-by-Step: Erase iPhone Before Selling</h2>
<ol>
<li><strong>Back up first</strong> — iCloud or local backup via Finder/iTunes</li>
<li><strong>Sign out of iCloud</strong> — Settings → [Your Name] → Sign Out</li>
<li><strong>Run Dr.Fone Data Eraser</strong> — Connect iPhone, choose "Erase All Data," select security level (we recommend Level 3: DoD overwrite)</li>
<li><strong>Download your erasure report</strong> — PDF with IMEI, timestamp, security level used</li>
<li><strong>Factory reset as final step</strong> — Settings → General → Transfer or Reset iPhone → Erase All Content</li>
</ol>
<h2>Why the Erasure Report Matters</h2>
<p>When selling on eBay, Swappa, or Facebook Marketplace, attaching a PDF erasure certificate increases buyer confidence and helps justify a higher price. It also protects you legally if the buyer later claims data was present on the device.</p>"""
    },
    {
        "slug": "erase-android-before-selling-2025",
        "title": "Erase Android Phone Before Selling — The Right Way",
        "date": "2025-06-08",
        "desc": "Android factory reset leaves data recoverable. Learn the correct permanent erase process for Samsung, Pixel, Xiaomi, and all major Android brands.",
        "content": """<p>Android's factory reset is even more inconsistent than Apple's — because Android is implemented differently by every manufacturer. Samsung, Google Pixel, Xiaomi, OPPO, and Motorola all handle storage encryption differently, meaning the risk level of a simple factory reset varies by device.</p>
<h2>The Samsung Problem</h2>
<p>Samsung Galaxy devices are the most targeted by data recovery efforts because they're the most common Android phone globally. Samsung's factory reset implementation on older devices (pre-Android 10) was particularly weak at destroying data. Third-party researchers have demonstrated recovery of contacts, photos, and banking app tokens from factory-reset Samsung phones purchased second-hand.</p>
<h2>What Android Versions Do</h2>
<p>Android 9 and earlier: Encryption optional, reset may not destroy keys. Android 10+: Full-disk encryption mandated, but reset behavior still varies. Android 12+: File-based encryption is standard, but key destruction at reset is still not guaranteed across all OEMs.</p>
<h2>How to Truly Wipe Any Android</h2>
<ol>
<li>Connect to Dr.Fone on Windows or Mac</li>
<li>Select "Erase All Data" for full wipe, or "Erase Private Data" for selective erase</li>
<li>Choose security level: 1-pass (fast), 3-pass (recommended for selling), or DoD 7-pass (maximum)</li>
<li>Let the tool overwrite all storage sectors</li>
<li>Download the erasure report PDF</li>
<li>Complete standard factory reset as a final step</li>
</ol>"""
    },
    {
        "slug": "dod-5220-22-m-explained",
        "title": "DoD 5220.22-M Explained in Plain Language",
        "date": "2025-06-10",
        "desc": "Military-grade data erasure sounds complicated. Here's what DoD 5220.22-M actually means, why it works, and when you need it.",
        "content": """<p>DoD 5220.22-M is the US Department of Defense's National Industrial Security Program Operating Manual. It defines standards for clearing and sanitizing classified storage media. The data sanitization section — which describes overwriting patterns — became the de facto standard for secure data deletion in commercial software.</p>
<h2>What the Standard Specifies</h2>
<p>The original DoD 5220.22-M spec called for three overwrite passes: first pass with 0x00, second pass with 0xFF, third pass with a random character, followed by a verification pass. This 3-pass method was designed for magnetic hard drives (HDDs).</p>
<h2>Does It Work on Flash Storage (SSDs and Phones)?</h2>
<p>Flash storage — NAND, which is what all phones use — doesn't map writes the same way as magnetic media. A modern phone's flash controller uses wear-leveling algorithms that distribute writes across the storage to prevent any single cell from being overwritten too frequently. This means a software overwrite command might not hit every physical storage cell.</p>
<p>This is why Dr.Fone's approach goes further: it combines overwrite passes with cryptographic key destruction and leverages OS-level secure erase commands that bypass the wear-leveling layer on supported devices.</p>
<h2>When Do You Actually Need Military-Grade Erasure?</h2>
<p>For personal use (selling a phone, giving to family), a single-pass overwrite plus factory reset is sufficient protection against casual data recovery. Three-pass DoD erasure is appropriate for: corporate device decommissioning, HIPAA-covered healthcare organizations, financial sector (PCI DSS compliance), government contractors. The seven-pass Gutmann method is overkill for flash storage but provides maximum documentation for compliance purposes.</p>"""
    },
    {
        "slug": "samsung-data-recovery-vulnerability",
        "title": "The Samsung Factory Reset Vulnerability: What You Need to Know",
        "date": "2025-06-12",
        "desc": "Samsung phones have a specific factory reset weakness that makes sold devices vulnerable. Here's the research and what to do about it.",
        "content": """<p>Samsung is the world's largest Android phone manufacturer. It's also the brand most commonly targeted in data recovery attempts on second-hand devices — and for good reason. Multiple independent security researchers have documented weaknesses in Samsung's factory reset implementation that leave user data recoverable.</p>
<h2>The Research</h2>
<p>Avast (now NortonLifeLock) purchased 20 used Android phones from eBay in 2014 and ran commercial data recovery software. They recovered over 40,000 photos (including intimate images), 750 emails and texts, and the identity of four previous owners — from phones that had been factory reset before sale.</p>
<p>A disproportionate number were Samsung devices. Follow-up research in 2018 and 2021 showed improvement on newer models with mandatory encryption, but the risk remains non-zero on older devices still in circulation.</p>
<h2>Which Samsung Devices Are Most at Risk</h2>
<p>Samsung Galaxy S7 and earlier (pre-2017): High risk — encryption optional, not enabled by default on many models. Galaxy S8 through S20: Medium risk — encryption standard, but forensic tools exist. Galaxy S21 and later with Android 12+: Lower risk — file-based encryption with improved key management.</p>
<h2>The Fix</h2>
<p>Don't rely on Samsung's factory reset alone. Use Dr.Fone Data Eraser to perform a DoD-standard overwrite before resetting. The tool supports all Samsung Galaxy models (S, A, Note series) and generates an erasure certificate confirming the wipe was performed.</p>"""
    },
    {
        "slug": "corporate-gdpr-hipaa-phone-erasure",
        "title": "Corporate Phone Disposal: GDPR, HIPAA, and PCI DSS Compliance Guide",
        "date": "2025-06-14",
        "desc": "IT managers and compliance officers: here's exactly what you need to do with company phones at end-of-life to meet regulatory requirements.",
        "content": """<p>When an employee leaves your company, their phone doesn't just go back into a drawer — it becomes a compliance liability. Every major data privacy regulation has specific requirements for how devices containing regulated data must be disposed of.</p>
<h2>GDPR (EU General Data Protection Regulation)</h2>
<p>Article 17 of GDPR — the "right to erasure" — applies not just to customer data requests but to your own devices. Any device that processed personal data of EU residents must be properly sanitized before disposal or reassignment. Failure to do so can result in fines of up to 4% of global annual turnover.</p>
<p>GDPR doesn't specify a technical standard for erasure, but ISO 27001 and NIST 800-88 are widely accepted as compliant methodologies.</p>
<h2>HIPAA (US Healthcare)</h2>
<p>The HIPAA Security Rule (45 CFR §164.310(d)(2)) requires covered entities to implement a media re-use policy that includes removal of PHI before reuse or disposal. The HHS guidance specifically recommends cryptographic erasure or overwriting for electronic media.</p>
<h2>PCI DSS</h2>
<p>PCI DSS Requirement 9.8.2 requires that electronic media be rendered unrecoverable when cardholder data is no longer needed. This applies to any device that ever processed, stored, or transmitted cardholder data — including phones used for mobile payment processing.</p>
<h2>The Compliance Workflow with Dr.Fone</h2>
<ol>
<li>Collect devices using chain-of-custody documentation</li>
<li>Run Dr.Fone Data Eraser with DoD 5220.22-M or higher standard</li>
<li>Download PDF erasure report for each device (includes IMEI, timestamp, security level)</li>
<li>Store reports for minimum 3 years (GDPR/HIPAA audit requirement)</li>
<li>Factory reset and re-provision or physically destroy the device</li>
</ol>
<p>Dr.Fone supports batch processing — multiple devices simultaneously — which is essential for IT departments managing dozens or hundreds of handsets.</p>"""
    },
    {
        "slug": "identity-theft-old-phone",
        "title": "Your Old Phone Is an Identity Theft Risk — Here's the Data",
        "date": "2025-06-16",
        "desc": "Sold phones are one of the top sources of identity theft. The data you think is gone is often still there. Here's what thieves actually recover.",
        "content": """<p>Identity theft costs Americans $56 billion annually, according to the FTC. A growing share of that — estimates range from 15% to 25% depending on the source — originates from improperly disposed electronics, including phones.</p>
<h2>What's Actually on Your Phone</h2>
<p>Most people underestimate what their phone contains. Beyond obvious things like photos and contacts, your phone holds: saved passwords and autofill data, banking and payment app session tokens (which can persist even after app uninstall), email and social media authentication cookies, biometric data registration files, location history (often years of it), corporate VPN credentials, and health data from fitness apps.</p>
<h2>How Thieves Use Recovered Data</h2>
<p>A recovered phone doesn't need to have your banking passwords visible in a notes app. Authentication tokens from your bank's mobile app — recovered from app data folders — can be replayed in some attack scenarios to gain account access without a password. Contacts lists are used for phishing and social engineering. Photos provide identity verification details (ID cards photographed for insurance, etc.).</p>
<h2>The Timeline Risk</h2>
<p>The average phone is sold within 2-4 weeks of purchase of a new device. Data recovery attacks typically happen within the first 30-60 days of a device appearing on the second-hand market — before the seller has moved on and is paying attention to unusual account activity.</p>
<h2>The Solution</h2>
<p>Permanently erasing your phone with Dr.Fone before selling takes about 20-30 minutes and costs less than a single fraudulent credit card charge to dispute. The erasure report PDF also gives you a documented record that you completed due diligence — valuable if any dispute arises later.</p>"""
    },
    {
        "slug": "erasure-report-guide",
        "title": "Data Erasure Reports: What They Are and Why They Matter",
        "date": "2025-06-18",
        "desc": "An erasure report isn't just paperwork. It proves your data is gone, helps resale value, and protects you legally. Here's everything you need to know.",
        "content": """<p>An erasure report (also called an erasure certificate or sanitization certificate) is a machine-generated PDF document that records the details of a secure data wipe. It's the digital equivalent of a signed receipt for data destruction.</p>
<h2>What a Good Erasure Report Contains</h2>
<ul>
<li><strong>Device identifiers</strong>: IMEI number, serial number, device model</li>
<li><strong>Erasure standard used</strong>: DoD 5220.22-M, NIST 800-88, etc.</li>
<li><strong>Security level</strong>: Number of overwrite passes</li>
<li><strong>Timestamp</strong>: Exact date and time of erasure</li>
<li><strong>Verification result</strong>: Confirmation that all sectors were successfully overwritten</li>
<li><strong>Software version</strong>: Which tool performed the erasure and its version number</li>
</ul>
<h2>Why It Matters for Resale</h2>
<p>On platforms like eBay, Swappa, and Back Market, listings with erasure certificates sell for 8-15% more and receive fewer buyer disputes. Buyers — especially tech-savvy ones — know factory reset isn't reliable. An erasure certificate signals that the seller took data security seriously and gives the buyer confidence the device is clean.</p>
<h2>Why It Matters for Business</h2>
<p>For corporate IT departments, erasure reports are audit artifacts. GDPR Article 30 requires records of processing activities. If your organization is audited following a data breach, erasure reports for properly decommissioned devices are evidence that you met your data minimization obligations.</p>
<h2>How to Get One</h2>
<p>Dr.Fone Data Eraser generates a PDF erasure report automatically at the end of every erase operation. The report is saved locally and can be printed or emailed. It includes all the fields listed above and is formatted to meet GDPR, HIPAA, and ISO 27001 documentation requirements.</p>"""
    },
    {
        "slug": "broken-phone-data-erase",
        "title": "How to Erase Data from a Broken Phone",
        "date": "2025-06-20",
        "desc": "Cracked screen, water damage, or won't turn on — your broken phone still has data on it. Here's how to erase it before recycling.",
        "content": """<p>A broken phone isn't a safely wiped phone. Whether the screen is shattered, the battery won't hold charge, or the phone won't boot at all — the NAND storage inside still contains all your data, fully intact and potentially recoverable.</p>
<h2>Scenarios and Solutions</h2>
<h3>Cracked Screen (Phone Still Powers On)</h3>
<p>If the phone can boot and connect via USB, Dr.Fone Data Eraser works normally. Connect via USB cable, grant USB debugging permission (you may need to use touch even with a damaged screen — some users use a USB OTG adapter with a mouse), and run the erase.</p>
<h3>Won't Boot (But Hardware Is Intact)</h3>
<p>If the phone enters recovery mode or fastboot mode, Dr.Fone can sometimes initiate a secure erase via ADB commands even when the OS won't boot normally. This works on most Android devices with USB debugging previously enabled.</p>
<h3>Water Damage</h3>
<p>Water-damaged phones that still function at all should be treated the same as a working phone — erase before recycling. If the phone is truly non-functional, the storage chip itself can potentially be removed and read by specialized recovery labs — a reason to prioritize erasure before the damage gets worse.</p>
<h3>Phone That Won't Turn On At All</h3>
<p>If a device is completely dead, the remaining option is physical destruction of the storage chip. Most phone recycling programs don't do this automatically — they sort, test, and resell working devices, and physically shred only devices deemed economically worthless. For phones with sensitive data that won't turn on, contact a certified e-waste facility that offers certificate of destruction for physical media shredding.</p>"""
    },
    {
        "slug": "three-security-levels-explained",
        "title": "Three Security Levels: Which One Do You Need?",
        "date": "2025-06-22",
        "desc": "Data eraser software offers multiple security levels. Here's what each one actually does, and which is right for your situation.",
        "content": """<p>Dr.Fone Data Eraser offers three security levels for data overwriting. Choosing the right one depends on how sensitive your data is and how much time you have.</p>
<h2>Level 1: Single Pass (Fast)</h2>
<p><strong>What it does:</strong> Overwrites every storage sector once with pseudorandom data.</p>
<p><strong>Time required:</strong> 10-15 minutes for a typical 64GB phone.</p>
<p><strong>Protection against:</strong> Consumer-grade data recovery software. Anyone who buys your phone and runs standard recovery apps will find nothing.</p>
<p><strong>Best for:</strong> Giving your phone to a family member, selling to a friend, general consumer use cases where you're not concerned about sophisticated attackers.</p>
<h2>Level 2: DoD Standard (Recommended)</h2>
<p><strong>What it does:</strong> Three overwrite passes — 0x00, 0xFF, random — following DoD 5220.22-M specification.</p>
<p><strong>Time required:</strong> 25-40 minutes for a typical device.</p>
<p><strong>Protection against:</strong> Professional data recovery services. This level would cost thousands of dollars in forensic lab time to attempt to circumvent, with no guarantee of success.</p>
<p><strong>Best for:</strong> Selling online to strangers, trade-in programs, giving away devices outside your trust circle. Recommended for most users in most situations.</p>
<h2>Level 3: Military Grade (Maximum)</h2>
<p><strong>What it does:</strong> Seven overwrite passes following the Gutmann method, plus DoD overwrite, plus cryptographic key destruction.</p>
<p><strong>Time required:</strong> 60-90 minutes.</p>
<p><strong>Protection against:</strong> State-level forensic analysis. Effectively renders data irrecoverable by any currently known method.</p>
<p><strong>Best for:</strong> Corporate compliance (HIPAA, GDPR, PCI DSS), IT department decommissioning, journalists or activists in high-risk environments, anyone with data of extraordinary sensitivity.</p>"""
    },
    {
        "slug": "selective-erase-iphone-guide",
        "title": "Selective Erase: Delete Specific Data from iPhone Without Factory Reset",
        "date": "2025-06-24",
        "desc": "Want to delete just photos, just messages, or just contacts from your iPhone — permanently — without wiping the whole device? Here's how.",
        "content": """<p>Full factory reset isn't always what you want. Sometimes you need to permanently delete specific categories of data — all photos, all messages to a specific contact, all banking app data — without resetting the entire phone. This is what selective erase is for.</p>
<h2>What You Can Selectively Erase</h2>
<p>Dr.Fone's "Erase Private Data" mode scans your iPhone and lets you permanently delete specific categories:</p>
<ul>
<li>Photos and videos (all, or specific albums)</li>
<li>Messages (SMS, iMessage, WhatsApp)</li>
<li>Contacts</li>
<li>Call history</li>
<li>Calendar events</li>
<li>Safari/browser history and cookies</li>
<li>App data (for installed apps)</li>
<li>Downloaded music and files</li>
</ul>
<h2>Why This Matters</h2>
<p>Standard iOS deletion (swipe to delete a photo, clear conversation history) doesn't permanently remove data. iOS keeps deleted items in "Recently Deleted" folders for up to 30 days, and even after that, the underlying storage blocks may remain readable until overwritten.</p>
<p>Selective erase with Dr.Fone overwrites only the targeted data, leaving the rest of your iPhone functional. This is ideal for: removing personal photos before giving your phone to a child, deleting sensitive conversations with a specific person, clearing app data from a banking or financial app you've stopped using.</p>
<h2>The Difference from Just Deleting</h2>
<p>Standard deletion: removes the file index entry, data remains on storage. Dr.Fone selective erase: overwrites the actual storage sectors where the data lived. The difference is the same as shredding a document versus throwing it in the recycling bin.</p>"""
    },
    {
        "slug": "phone-junk-cleanup-guide",
        "title": "Clean Your Phone Storage Without Losing Personal Data",
        "date": "2025-06-26",
        "desc": "Full storage slowing you down? Here's how to safely delete junk files, cache, temp files, and duplicates without touching your important data.",
        "content": """<p>The average smartphone accumulates several gigabytes of junk files per year: app cache, temp download files, browser data, duplicate photos, and orphaned app data from uninstalled apps. This junk doesn't just waste space — it can slow down your device and contribute to app crashes.</p>
<h2>Types of Junk Files on Your Phone</h2>
<p><strong>App cache:</strong> Temporary files apps create to load faster. Often safe to delete; apps will rebuild on next use. Some apps (Facebook, Spotify) accumulate hundreds of MB of cache.</p>
<p><strong>Temp files:</strong> Files created during downloads or app operations that weren't cleaned up. Always safe to delete.</p>
<p><strong>Duplicate photos:</strong> Multiple copies of the same image from Live Photos, burst mode, or backups. Easy to accumulate thousands without noticing.</p>
<p><strong>Orphaned app data:</strong> Files left behind by uninstalled apps. Some apps don't clean up after themselves on uninstall, leaving GB of data with no associated app.</p>
<p><strong>Browser cache and cookies:</strong> Websites store data locally for faster reload. Can grow to hundreds of MB on actively used browsers.</p>
<h2>Safe Cleanup vs. Risky Cleanup</h2>
<p>Always safe: temp files, app cache, orphaned data, browser cache. Usually safe with review: duplicate photos (check before deleting). Risky if done wrong: app data (may delete saved settings or offline content).</p>
<p>Dr.Fone's junk cleaner scans your device and categorizes files by type before you delete anything. Unlike some aggressive cleaners that delete first and ask questions never, it shows you exactly what it found so you can decide what to remove.</p>"""
    },
    {
        "slug": "erase-before-trade-in-guide",
        "title": "Erase Phone Before Trade-In: Carrier and Retailer Programs Explained",
        "date": "2025-06-28",
        "desc": "Trading in at Apple, Samsung, Verizon, AT&T, or Best Buy? Here's what to do before handing over your phone — and what these programs don't tell you.",
        "content": """<p>Phone trade-in programs are convenient, but they have a dirty secret: they don't securely erase your data. Most carrier and retailer trade-in programs instruct customers to perform a factory reset — and nothing more — before handing over the device. As we've covered, factory reset is not enough.</p>
<h2>What Major Programs Actually Do with Your Device</h2>
<p><strong>Apple Trade In:</strong> Apple instructs you to back up and erase via Settings. Apple's own erasure (on hardware-encrypted devices) is stronger than average, but not DoD-compliant.</p>
<p><strong>Carrier programs (Verizon, AT&T, T-Mobile):</strong> Typically instruct you to factory reset. The carrier does not perform additional erasure — devices are shipped to third-party refurbishers.</p>
<p><strong>Best Buy, Walmart:</strong> Same as above. Factory reset only instructions. Devices go to wholesale buyers who resell them.</p>
<p><strong>Third-party programs (Gazelle, Decluttr, SellCell):</strong> These programs receive your device in whatever state you send it. Better ones may perform a reset before resale; most do not advertise secure erasure standards.</p>
<h2>The Right Sequence</h2>
<ol>
<li>Back up your data to your new device or iCloud/Google</li>
<li>Run Dr.Fone Data Eraser — full erase, DoD standard</li>
<li>Save your erasure certificate PDF</li>
<li>Perform the carrier/retailer's requested factory reset</li>
<li>Hand over the device</li>
</ol>
<p>This sequence takes 30-45 minutes and eliminates the risk entirely, regardless of what the trade-in program does (or doesn't do) with your device afterward.</p>"""
    },
    {
        "slug": "best-data-eraser-software-2025",
        "title": "Best Data Eraser Software 2025 — Ranked and Compared",
        "date": "2025-06-30",
        "desc": "We compared the top phone data erasure tools on features, security level, device support, and certification. Here's what we found.",
        "content": """<p>Not all data eraser software is equal. Some offer a single overwrite pass and call it "military grade." Others support only a handful of devices. Here's how the leading options compare in 2025.</p>
<h2>Evaluation Criteria</h2>
<p>We evaluated tools on: supported devices, security levels offered, erasure certification/reporting, selective erase capability, junk cleanup features, and platform (Windows/Mac).</p>
<h2>Dr.Fone Data Eraser (Wondershare)</h2>
<p><strong>Devices:</strong> 1,000+ iOS and Android devices. <strong>Security levels:</strong> 1-pass, DoD 3-pass, 7-pass. <strong>Erasure report:</strong> Yes, PDF with IMEI and timestamp. <strong>Selective erase:</strong> Yes. <strong>Junk cleanup:</strong> Yes. <strong>Platform:</strong> Windows and Mac. <strong>Verdict:</strong> Most comprehensive option for personal and business use.</p>
<h2>iMobie PhoneClean</h2>
<p><strong>Devices:</strong> iOS only. <strong>Security levels:</strong> Single pass. <strong>Erasure report:</strong> No. <strong>Selective erase:</strong> Yes. <strong>Verdict:</strong> Good for iOS junk cleanup; limited for security-focused erasure.</p>
<h2>Stellar Data Eraser</h2>
<p><strong>Devices:</strong> Android only. <strong>Security levels:</strong> Multiple. <strong>Erasure report:</strong> Yes. <strong>Verdict:</strong> Solid Android option; no iOS support limits versatility.</p>
<h2>Manual Factory Reset</h2>
<p><strong>Devices:</strong> Any. <strong>Security levels:</strong> Unreliable. <strong>Erasure report:</strong> None. <strong>Verdict:</strong> Not recommended for any situation where data sensitivity matters.</p>"""
    },
    {
        "slug": "pc-file-shredder-guide",
        "title": "How to Permanently Delete Files on Windows and Mac",
        "date": "2025-07-02",
        "desc": "Deleted files aren't really deleted. Here's how to permanently overwrite and shred files on Windows 10/11 and macOS so they can't be recovered.",
        "content": """<p>When you delete a file on Windows or Mac \u2014 even emptying the recycle bin \u2014 the file isn't erased. The operating system simply marks that storage space as available and removes the file's entry from the directory. The actual data remains intact on the drive until new data overwrites those sectors.</p>
<h2>How File Recovery Works Against You</h2>
<p>File recovery tools like Recuva (Windows) or PhotoRec (cross-platform) scan your drive for these orphaned data blocks and reassemble files that were "deleted" weeks or months ago. Anyone with access to your PC — or your old hard drive after you sell it — can run these tools and potentially recover documents, photos, financial records, and more.</p>
<h2>Windows: How to Truly Delete Files</h2>
<p><strong>Built-in option — Cipher:</strong> <code>cipher /w:C:\</code> in Command Prompt overwrites free space on the C: drive. Slow but free. <strong>Better option — Dr.Fone on PC:</strong> Supports file-level shredding and free-space wipe with DoD-compliant overwrite passes. Also handles the phone erasure in the same software.</p>
<h2>Mac: Secure Empty Trash</h2>
<p>Apple removed the "Secure Empty Trash" option in macOS Sierra. The reasoning was that SSDs make traditional overwriting unreliable due to wear leveling. For Macs with SSDs (all models from 2013 onward), the recommended approach is FileVault encryption plus erase — the same cryptographic erasure approach Dr.Fone uses for phone storage.</p>
<h2>Before Selling Your Computer</h2>
<p>Before selling or donating a PC or Mac: enable full-disk encryption if not already active, perform a DoD overwrite of all free space, then reset the OS to factory. For SSDs specifically, look for manufacturer secure erase utilities (Samsung Magician, Intel SSD Toolbox) in addition to software overwriting.</p>"""
    },
]

print(f"Blog posts: {len(BLOG_POSTS)}")

# ═══════════════════════════════════════════════════════════════
#  ESSENTIAL PAGES
# ═══════════════════════════════════════════════════════════════
ESSENTIAL_PAGES = [
    "index", "about", "contact", "privacy", "terms",
    "sitemap", "blog", "categories", "faq", "download", "glossary",
]

# ═══════════════════════════════════════════════════════════════
#  CSS / DESIGN  (dark crimson on deep charcoal)
# ═══════════════════════════════════════════════════════════════
CSS = """
:root {
  --bg:        #0f172a;
  --bg2:       #1e293b;
  --bg3:       #0d1424;
  --accent:    #dc2626;
  --accent2:   #b91c1c;
  --accent3:   #ef4444;
  --text:      #f1f5f9;
  --muted:     #94a3b8;
  --border:    #334155;
  --radius:    8px;
  --font:      'Inter', system-ui, sans-serif;
  --mono:      'JetBrains Mono', monospace;
  --max:       1200px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  font-size: 16px;
  line-height: 1.7;
  min-height: 100vh;
}
a { color: var(--accent3); text-decoration: none; }
a:hover { text-decoration: underline; }
img { max-width: 100%; }

/* ── TOPBAR ALERT ── */
.topbar {
  background: var(--accent);
  text-align: center;
  padding: 10px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}
.topbar a { color: #fff; text-decoration: underline; }

/* ── NAV ── */
nav {
  background: var(--bg3);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 100;
}
.nav-inner {
  max-width: var(--max);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 60px;
}
.logo {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text) !important;
  text-decoration: none !important;
  display: flex;
  align-items: center;
  gap: 8px;
}
.logo-icon {
  width: 28px; height: 28px;
  background: var(--accent);
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.9rem;
}
.nav-links {
  display: flex;
  gap: 8px;
  align-items: center;
}
.nav-links a {
  color: var(--muted);
  font-size: 0.85rem;
  padding: 6px 12px;
  border-radius: var(--radius);
  transition: color .15s, background .15s;
}
.nav-links a:hover { color: var(--text); background: var(--bg2); text-decoration: none; }
.btn-nav {
  background: var(--accent);
  color: #fff !important;
  padding: 8px 18px !important;
  border-radius: var(--radius) !important;
  font-weight: 700;
  font-size: 0.85rem;
}
.btn-nav:hover { background: var(--accent2) !important; }

/* ── HERO ── */
.hero {
  background: linear-gradient(135deg, #0d1424 0%, #1a0a0a 50%, #0d1424 100%);
  padding: 100px 24px 80px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 60% at 50% 40%, rgba(220,38,38,.15) 0%, transparent 70%);
  pointer-events: none;
}
.hero-eyebrow {
  display: inline-block;
  background: rgba(220,38,38,.15);
  border: 1px solid rgba(220,38,38,.4);
  color: var(--accent3);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 6px 16px;
  border-radius: 999px;
  margin-bottom: 24px;
  animation: pulse-border 2.5s infinite;
}
@keyframes pulse-border {
  0%, 100% { border-color: rgba(220,38,38,.4); }
  50%       { border-color: rgba(220,38,38,.9); }
}
.hero h1 {
  font-size: clamp(2rem, 5vw, 3.6rem);
  font-weight: 900;
  line-height: 1.15;
  max-width: 800px;
  margin: 0 auto 20px;
  letter-spacing: -0.02em;
}
.hero h1 .accent { color: var(--accent3); }
.hero-sub {
  font-size: 1.15rem;
  color: var(--muted);
  max-width: 580px;
  margin: 0 auto 40px;
}
.btn-primary {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  padding: 16px 36px;
  border-radius: var(--radius);
  font-weight: 800;
  font-size: 1.05rem;
  transition: background .15s, transform .1s;
  cursor: pointer;
}
.btn-primary:hover { background: var(--accent2); transform: translateY(-2px); text-decoration: none; }
.btn-secondary {
  display: inline-block;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
  padding: 14px 32px;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 1rem;
  margin-left: 12px;
  transition: border-color .15s, background .15s;
}
.btn-secondary:hover { border-color: var(--accent); background: rgba(220,38,38,.08); text-decoration: none; }
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 48px;
  margin-top: 64px;
  flex-wrap: wrap;
}
.stat { text-align: center; }
.stat-num {
  display: block;
  font-size: 2.2rem;
  font-weight: 900;
  color: var(--accent3);
  line-height: 1;
}
.stat-lbl { font-size: 0.8rem; color: var(--muted); margin-top: 4px; }

/* ── SECTIONS ── */
section { padding: 80px 24px; }
.container { max-width: var(--max); margin: 0 auto; }
.section-eyebrow {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent3);
  margin-bottom: 12px;
}
h2 {
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 800;
  line-height: 1.25;
  margin-bottom: 16px;
}
.section-lead {
  color: var(--muted);
  font-size: 1.05rem;
  max-width: 640px;
  margin-bottom: 48px;
}

/* ── DANGER SECTION ── */
.danger-section {
  background: radial-gradient(ellipse 80% 80% at 50% 50%, rgba(185,28,28,.12) 0%, transparent 70%), var(--bg3);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.danger-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}
.danger-card {
  background: rgba(220,38,38,.06);
  border: 1px solid rgba(220,38,38,.2);
  border-radius: var(--radius);
  padding: 28px;
  transition: border-color .2s;
}
.danger-card:hover { border-color: rgba(220,38,38,.5); }
.danger-icon { font-size: 1.8rem; margin-bottom: 12px; }
.danger-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 8px; }
.danger-card p { font-size: 0.875rem; color: var(--muted); }

/* ── FEATURES ── */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
.feature-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-top: 3px solid transparent;
  border-radius: var(--radius);
  padding: 28px;
  transition: border-top-color .2s, transform .15s;
}
.feature-card:hover { border-top-color: var(--accent); transform: translateY(-3px); }
.feature-icon { font-size: 1.6rem; margin-bottom: 12px; }
.feature-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 8px; }
.feature-card p { font-size: 0.875rem; color: var(--muted); }

/* ── HOW IT WORKS ── */
.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 32px;
}
.step { text-align: center; }
.step-num {
  width: 48px; height: 48px;
  background: var(--accent);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 900; font-size: 1.1rem;
  margin: 0 auto 16px;
}
.step h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 8px; }
.step p { font-size: 0.85rem; color: var(--muted); }

/* ── COMPARISON TABLE ── */
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
th {
  background: var(--bg2);
  padding: 14px 16px;
  text-align: left;
  font-weight: 700;
  border-bottom: 2px solid var(--border);
  white-space: nowrap;
}
th.highlight { background: rgba(220,38,38,.15); color: var(--accent3); }
td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  color: var(--muted);
}
tr:last-child td { border-bottom: none; }
td.highlight { color: var(--text); font-weight: 600; }
.check { color: #22c55e; font-weight: 700; }
.cross { color: #ef4444; }

/* ── BLOG ── */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}
.blog-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  transition: border-color .2s, transform .15s;
}
.blog-card:hover { border-color: var(--accent); transform: translateY(-3px); }
.blog-cat {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--accent3);
  margin-bottom: 10px;
}
.blog-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 8px; line-height: 1.4; }
.blog-card p { font-size: 0.85rem; color: var(--muted); margin-bottom: 16px; }
.blog-date { font-size: 0.78rem; color: var(--muted); }

/* ── FAQ ── */
.faq-list { max-width: 760px; }
.faq-item {
  border-bottom: 1px solid var(--border);
  padding: 20px 0;
}
.faq-q {
  font-weight: 700;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}
.faq-toggle { color: var(--accent3); flex-shrink: 0; font-size: 1.2rem; }
.faq-a { color: var(--muted); font-size: 0.9rem; margin-top: 12px; display: none; }
.faq-item.open .faq-a { display: block; }
.faq-item.open .faq-toggle { transform: rotate(45deg); }

/* ── GLOSSARY ── */
.glossary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
.gloss-item {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px 20px;
}
.gloss-term { font-weight: 700; color: var(--accent3); font-size: 0.9rem; margin-bottom: 4px; }
.gloss-def { font-size: 0.82rem; color: var(--muted); }

/* ── CTA BAND ── */
.cta-band {
  background: linear-gradient(135deg, #1a0505, #0f172a 60%);
  border-top: 1px solid rgba(220,38,38,.3);
  border-bottom: 1px solid rgba(220,38,38,.3);
  padding: 80px 24px;
  text-align: center;
}
.cta-band h2 { margin-bottom: 16px; }
.cta-band p { color: var(--muted); margin-bottom: 32px; max-width: 520px; margin-left: auto; margin-right: auto; }

/* ── SECURITY BADGES ── */
.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  margin-top: 32px;
}
.badge {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 8px 16px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--muted);
}

/* ── BREADCRUMB ── */
.breadcrumb {
  padding: 12px 24px;
  background: var(--bg3);
  border-bottom: 1px solid var(--border);
  font-size: 0.8rem;
  color: var(--muted);
}
.breadcrumb a { color: var(--muted); }
.breadcrumb a:hover { color: var(--accent3); }

/* ── KW PAGE ── */
.kw-hero {
  padding: 64px 24px 48px;
  background: linear-gradient(180deg, var(--bg3) 0%, var(--bg) 100%);
  border-bottom: 1px solid var(--border);
}
.kw-hero h1 { font-size: clamp(1.6rem, 3.5vw, 2.6rem); font-weight: 900; margin-bottom: 16px; }
.kw-hero p { color: var(--muted); max-width: 640px; }
.kw-body { max-width: var(--max); margin: 0 auto; padding: 48px 24px; }
.kw-body h2 { font-size: 1.4rem; margin: 32px 0 12px; }
.kw-body p, .kw-body li { color: var(--muted); font-size: 0.95rem; margin-bottom: 10px; }
.kw-body ul, .kw-body ol { padding-left: 20px; margin-bottom: 16px; }
.kw-body li { margin-bottom: 6px; }

/* ── BLOG POST ── */
.post-hero {
  padding: 80px 24px 56px;
  background: var(--bg3);
  border-bottom: 1px solid var(--border);
  max-width: 800px;
  margin: 0 auto;
}
.post-hero h1 { font-size: clamp(1.6rem, 3vw, 2.4rem); font-weight: 900; line-height: 1.3; margin-bottom: 16px; }
.post-meta { font-size: 0.82rem; color: var(--muted); }
.post-body {
  max-width: 760px;
  margin: 0 auto;
  padding: 48px 24px 80px;
}
.post-body h2 { font-size: 1.35rem; margin: 36px 0 14px; }
.post-body h3 { font-size: 1.1rem; margin: 28px 0 10px; color: var(--text); }
.post-body p { color: var(--muted); margin-bottom: 16px; font-size: 0.95rem; }
.post-body ul, .post-body ol { padding-left: 22px; margin-bottom: 16px; }
.post-body li { color: var(--muted); font-size: 0.95rem; margin-bottom: 6px; }
.post-body strong { color: var(--text); }
.post-body code { background: var(--bg2); padding: 2px 6px; border-radius: 4px; font-family: var(--mono); font-size: 0.88em; }
.post-cta {
  background: rgba(220,38,38,.08);
  border: 1px solid rgba(220,38,38,.25);
  border-radius: var(--radius);
  padding: 28px;
  margin: 40px 0;
  text-align: center;
}
.post-cta p { color: var(--text); font-weight: 600; margin-bottom: 16px; }

/* ── FOOTER ── */
footer {
  background: var(--bg3);
  border-top: 1px solid var(--border);
  padding: 56px 24px 32px;
}
.footer-grid {
  max-width: var(--max);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}
.footer-brand p { color: var(--muted); font-size: 0.85rem; margin-top: 12px; max-width: 280px; }
.footer-col h4 { font-size: 0.85rem; font-weight: 700; margin-bottom: 16px; color: var(--text); }
.footer-col ul { list-style: none; }
.footer-col li { margin-bottom: 8px; }
.footer-col a { color: var(--muted); font-size: 0.83rem; transition: color .15s; }
.footer-col a:hover { color: var(--accent3); text-decoration: none; }
.footer-bottom {
  max-width: var(--max);
  margin: 0 auto;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.78rem;
  color: var(--muted);
}
.footer-bottom a { color: var(--muted); }
.footer-bottom a:hover { color: var(--accent3); text-decoration: none; }

/* ── RESPONSIVE ── */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero-stats { gap: 24px; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .btn-secondary { margin: 12px 0 0; }
}
@media (max-width: 480px) {
  .footer-grid { grid-template-columns: 1fr; }
}
"""

# ═══════════════════════════════════════════════════════════════
#  SHARED HTML COMPONENTS
# ═══════════════════════════════════════════════════════════════
def nav_html(active=""):
    cats_sample = [
        ("Erase Before Selling","erase-before-selling"),
        ("iPhone Erase","iphone-erase"),
        ("Android Erase","android-erase"),
        ("Business","business-compliance"),
    ]
    links = "".join(f'<a href="{BASE_PATH}/category/{c[1]}/">{c[0]}</a>' for c in cats_sample)
    return f"""
<div class="topbar">
  ⚠️ Factory reset leaves your data recoverable.
  <a href="{AFFILIATE_URL}" target="_blank" rel="noopener">Get Dr.Fone Data Eraser — erase it for real →</a>
</div>
<nav>
  <div class="nav-inner">
    <a class="logo" href="{BASE_PATH}/"><span class="logo-icon">🔒</span> DataEraserOnline</a>
    <div class="nav-links">
      {links}
      <a href="{BASE_PATH}/blog/">Blog</a>
      <a href="{BASE_PATH}/faq/">FAQ</a>
      <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-nav">Free Download</a>
    </div>
  </div>
</nav>"""

def footer_html():
    cat_list = [
        ("brand","Brand"),("erase-before-selling","Erase Before Selling"),
        ("iphone-erase","iPhone Erase"),("android-erase","Android Erase"),
        ("privacy-protection","Privacy Protection"),("junk-cleanup","Junk Cleanup"),
        ("erasure-report","Erasure Report"),("compare","Compare"),
        ("howto","How-To"),("platform","Platform"),
        ("pc-file-erase","PC File Erase"),("broken-phone","Broken Phone"),
        ("business-compliance","Business Compliance"),("global","Global"),
        ("usecase","Use Cases"),
    ]
    cat_links = "".join(f'<li><a href="{BASE_PATH}/category/{s}/">{n}</a></li>' for s,n in cat_list[:8])
    blog_links = "".join(f'<li><a href="{BASE_PATH}/blog/{b["slug"]}/">{b["title"][:45]}…</a></li>' for b in BLOG_POSTS[:5])
    return f"""
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <a class="logo" href="{BASE_PATH}/" style="font-size:1rem"><span class="logo-icon">🔒</span> DataEraserOnline</a>
      <p>Independent guide to permanently erasing phone and PC data. Affiliated with Wondershare Dr.Fone Data Eraser.</p>
    </div>
    <div class="footer-col">
      <h4>Categories</h4>
      <ul>{cat_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Recent Posts</h4>
      <ul>{blog_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Site</h4>
      <ul>
        <li><a href="{BASE_PATH}/">Home</a></li>
        <li><a href="{BASE_PATH}/blog/">Blog</a></li>
        <li><a href="{BASE_PATH}/faq/">FAQ</a></li>
        <li><a href="{BASE_PATH}/glossary/">Glossary</a></li>
        <li><a href="{BASE_PATH}/categories/">All Categories</a></li>
        <li><a href="{BASE_PATH}/about/">About</a></li>
        <li><a href="{BASE_PATH}/contact/">Contact</a></li>
        <li><a href="{BASE_PATH}/privacy/">Privacy Policy</a></li>
        <li><a href="{BASE_PATH}/terms/">Terms</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© {YEAR} DataEraserOnline.com — Independent Review Site</span>
    <span>Affiliate disclosure: We earn a commission from Dr.Fone purchases at no cost to you.</span>
    <a href="{BASE_PATH}/sitemap.xml">Sitemap</a>
  </div>
</footer>"""

def page(title, desc, canonical, body, schema="", og_type="website"):
    schema_tag = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta name="robots" content="index,follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
{schema_tag}
</head>
<body>
{nav_html()}
{body}
{footer_html()}
<script>
document.querySelectorAll('.faq-q').forEach(q => {{
  q.addEventListener('click', () => q.parentElement.classList.toggle('open'));
}});
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════════
#  PAGE BUILDERS
# ═══════════════════════════════════════════════════════════════
COMPARISON_TABLE = """
<div class="table-wrap">
<table>
<thead>
<tr>
  <th>Feature</th>
  <th class="highlight">Dr.Fone Eraser</th>
  <th>Factory Reset</th>
  <th>iMobie</th>
  <th>Stellar</th>
</tr>
</thead>
<tbody>
<tr><td>iOS Support</td><td class="highlight check">✓ All versions</td><td class="check">✓</td><td class="check">✓</td><td class="cross">✗</td></tr>
<tr><td>Android Support</td><td class="highlight check">✓ 1,000+ devices</td><td class="check">✓</td><td class="cross">✗</td><td class="check">✓</td></tr>
<tr><td>DoD 5220.22-M</td><td class="highlight check">✓</td><td class="cross">✗</td><td class="cross">✗</td><td class="check">✓</td></tr>
<tr><td>7-Pass Overwrite</td><td class="highlight check">✓</td><td class="cross">✗</td><td class="cross">✗</td><td class="cross">✗</td></tr>
<tr><td>Erasure Report PDF</td><td class="highlight check">✓ with IMEI</td><td class="cross">✗</td><td class="cross">✗</td><td class="check">✓</td></tr>
<tr><td>Selective Erase</td><td class="highlight check">✓</td><td class="cross">✗</td><td class="check">✓</td><td class="cross">✗</td></tr>
<tr><td>Junk Cleaner</td><td class="highlight check">✓</td><td class="cross">✗</td><td class="check">✓</td><td class="cross">✗</td></tr>
<tr><td>GDPR/HIPAA Docs</td><td class="highlight check">✓</td><td class="cross">✗</td><td class="cross">✗</td><td class="check">✓</td></tr>
<tr><td>Broken Phone</td><td class="highlight check">✓ (partial)</td><td class="cross">✗</td><td class="cross">✗</td><td class="cross">✗</td></tr>
<tr><td>Windows + Mac</td><td class="highlight check">✓</td><td class="cross">N/A</td><td class="check">✓</td><td class="check">✓</td></tr>
</tbody>
</table>
</div>"""

FEATURES = [
    ("🔒","Military-Grade Erasure","DoD 5220.22-M with 1, 3, or 7 overwrite passes. Data is gone — not just hidden."),
    ("📋","Erasure Report PDF","Certificate with IMEI, timestamp, and security level for every wipe. Essential for compliance and resale."),
    ("🎯","Selective Erase","Delete only photos, messages, or contacts — permanently — without resetting the whole phone."),
    ("🗑️","Junk File Cleaner","Remove cache, temp files, and duplicates safely. Free up GB of storage without touching personal data."),
    ("📸","Photo Compressor","Lossless compression reduces photo file sizes up to 75%. Keep quality, reclaim space."),
    ("📱","1,000+ Devices","All iPhone and iPad models (iOS 7+) plus all major Android brands — Samsung, Pixel, Xiaomi, OPPO."),
    ("🏢","Business Compliance","Batch erase, chain-of-custody workflow, GDPR/HIPAA documentation. Built for IT departments."),
    ("💔","Broken Phone Support","Wipe cracked, water-damaged, or non-booting phones via USB + ADB. Don't let damage mean data exposure."),
]

DANGER_ITEMS = [
    ("⚠️","Factory Reset Leaves Data","The file directory is cleared — but the actual data blocks on NAND storage remain, readable by any recovery tool."),
    ("🔍","Data Recovery Is Cheap","Professional-grade data recovery software costs under $50. Anyone who buys your phone can run it."),
    ("🏦","Financial Data at Risk","Banking app tokens, saved autofill passwords, and payment credentials survive factory reset."),
    ("🪪","Identity Theft Waiting","Photos of IDs, passports, and license plates. Contacts for social engineering. All recoverable."),
]

FAQ_ITEMS = [
    ("Is factory reset enough before selling my phone?",
     "No. Factory reset removes the file directory but does not overwrite the actual data on flash storage. Recovery software can reconstruct files from factory-reset devices. Cambridge University researchers demonstrated this on Android phones; Apple's hardware encryption is stronger but not immune to forensic tools."),
    ("How long does a secure erase take?",
     "Level 1 (single pass): 10-20 minutes. Level 2 (DoD 3-pass): 25-45 minutes. Level 3 (7-pass military): 60-90 minutes. Times vary by device storage size and write speed."),
    ("Will erasing my phone remove the operating system?",
     "No. Dr.Fone erases your personal data — photos, messages, contacts, app data — and overwrites the storage sectors they occupied. A factory reset at the end restores the OS. The new owner receives a blank phone, not a bricked one."),
    ("Is Dr.Fone Data Eraser safe to use?",
     "Yes. Dr.Fone is made by Wondershare, a publicly listed company founded in 2003 with over 100 million users worldwide. The software is digitally signed, available on Windows and Mac, and does not require root or jailbreak."),
    ("Can I erase just some data and keep the rest?",
     "Yes. Dr.Fone's 'Erase Private Data' mode lets you choose specific categories — photos, messages, contacts, browser history, app data — and permanently overwrites only those items, leaving the rest of your phone intact."),
    ("Does the erasure report work for GDPR compliance?",
     "Yes. The PDF erasure report includes device IMEI, serial number, timestamp, security level, and pass/fail status — the fields required by ISO 27001 and accepted by GDPR auditors as evidence of proper device sanitization."),
    ("Can I erase a broken or cracked phone?",
     "Partially. If the phone powers on and connects via USB, Dr.Fone can erase it normally despite a broken screen. Phones that won't boot may be erasable via ADB commands if USB debugging was previously enabled. Completely dead devices may require physical storage destruction."),
    ("How many devices can I erase with one license?",
     "License terms vary — check the Dr.Fone website for current plans. Business licenses support unlimited devices and batch processing."),
]

GLOSSARY_TERMS = [
    ("DoD 5220.22-M","US Department of Defense data sanitization standard specifying overwrite patterns for storage media."),
    ("NIST 800-88","NIST guidelines for media sanitization, widely used for government and enterprise compliance."),
    ("Cryptographic Erasure","Destroying encryption keys rather than overwriting data — effective on encrypted storage like modern iPhones."),
    ("Factory Reset","OS-level reset that removes the file directory but does not overwrite underlying data on storage."),
    ("NAND Flash","Type of storage used in all smartphones. Data written to NAND cells persists after deletion until overwritten."),
    ("Wear Leveling","Flash storage controller algorithm that distributes writes across cells, complicating overwrite-based erasure."),
    ("Erasure Certificate","Machine-generated PDF documenting a completed secure wipe, used for compliance audits."),
    ("IMEI","International Mobile Equipment Identity — unique 15-digit hardware ID printed on every phone."),
    ("Secure Element","Dedicated chip on iPhones (Secure Enclave) that manages encryption keys for hardware-based protection."),
    ("ADB","Android Debug Bridge — command-line tool enabling PC communication with Android devices for advanced operations."),
    ("GDPR Article 17","EU regulation right-to-erasure provision requiring data controllers to permanently delete personal data when requested."),
    ("HIPAA PHI","Protected Health Information — medical data requiring secure disposal under US HIPAA Security Rule."),
    ("PCI DSS","Payment Card Industry Data Security Standard — requires secure disposal of devices that processed cardholder data."),
    ("Overwrite Pass","Single cycle of writing data (0x00, 0xFF, or random) across all storage sectors to obscure previous content."),
    ("File Allocation Table","Index structure telling the OS where files are stored; factory reset clears this but not the underlying data."),
    ("Selective Erase","Permanent deletion of specific data categories (photos, messages) without performing a full factory reset."),
    ("Forensic Recovery","Use of specialized tools to reconstruct files from storage that has been deleted or factory-reset."),
    ("ISO 27001","International information security standard whose asset disposal requirements are met by certified erasure reports."),
    ("USB Debugging","Android developer mode that enables ADB communication; required for some erasure methods on damaged devices."),
    ("Junk Files","App cache, temp files, and orphaned data that waste storage but contain no user-created content."),
    ("Biometric Data","Face ID and fingerprint templates stored on-device; must be erased before device transfer for privacy."),
    ("Authentication Token","Session credential stored by apps; can allow account access without passwords if recovered from storage."),
    ("Bulk Erasure","Simultaneous secure wipe of multiple devices, used by IT departments during employee offboarding."),
    ("E-waste","Electronic waste — improperly disposed devices are a leading source of data breaches and identity theft."),
    ("Chain of Custody","Documentation tracking who handled a device and when, required for corporate compliance workflows."),
]

HOW_IT_WORKS = [
    ("1","Connect Your Device","Plug your iPhone or Android into your PC or Mac via USB cable. Dr.Fone detects the device automatically."),
    ("2","Choose Erase Mode","Select Full Erase (all data) or Selective Erase (specific categories). Choose your security level."),
    ("3","Confirm and Erase","Confirm the operation. Dr.Fone overwrites every storage sector using your chosen DoD standard."),
    ("4","Download Report","Get your PDF erasure certificate with IMEI, timestamp, and security level. Done."),
]

def homepage():
    danger_cards = "".join(f'<div class="danger-card"><div class="danger-icon">{ic}</div><h3>{h}</h3><p>{p}</p></div>' for ic,h,p in DANGER_ITEMS)
    feat_cards   = "".join(f'<div class="feature-card"><div class="feature-icon">{ic}</div><h3>{h}</h3><p>{p}</p></div>' for ic,h,p in FEATURES)
    steps_html   = "".join(f'<div class="step"><div class="step-num">{n}</div><h3>{h}</h3><p>{p}</p></div>' for n,h,p in HOW_IT_WORKS)
    faq_html     = "".join(f'<div class="faq-item"><div class="faq-q">{q}<span class="faq-toggle">+</span></div><div class="faq-a">{a}</div></div>' for q,a in FAQ_ITEMS[:6])
    blog_preview = "".join(f'<div class="blog-card"><div class="blog-cat">Research</div><h3><a href="{BASE_PATH}/blog/{b["slug"]}/">{b["title"]}</a></h3><p>{b["desc"]}</p><div class="blog-date">{b["date"]}</div></div>' for b in BLOG_POSTS[:6])
    cats_by = defaultdict(list)
    for kwd in KEYWORDS: cats_by[kwd["cat"]].append(kwd)
    cat_cards = ""
    cat_names = {
        "brand":"Brand","erase-before-selling":"Erase Before Selling","iphone-erase":"iPhone Erase",
        "android-erase":"Android Erase","privacy-protection":"Privacy","junk-cleanup":"Junk Cleanup",
        "erasure-report":"Erasure Reports","compare":"Compare","howto":"How-To","platform":"Platform",
        "pc-file-erase":"PC File Erase","broken-phone":"Broken Phone","business-compliance":"Business",
        "global":"Global","usecase":"Use Cases",
    }
    for cat, kws in sorted(cats_by.items(), key=lambda x: -len(x[1]))[:12]:
        n = cat_names.get(cat, cat.title())
        cat_cards += f'<div class="blog-card"><div class="blog-cat">{len(kws)} keywords</div><h3><a href="{BASE_PATH}/category/{cat}/">{n}</a></h3><p>Browse all {n.lower()} guides and how-to articles.</p></div>'

    schema = json.dumps({
        "@context":"https://schema.org","@type":"WebSite",
        "name":"DataEraserOnline","url":SITE_DOMAIN,
        "potentialAction":{"@type":"SearchAction","target":f"{SITE_DOMAIN}/search?q={{search_term_string}}","query-input":"required name=search_term_string"}
    })
    body = f"""
<section class="hero">
  <div style="position:relative;z-index:1">
    <div class="hero-eyebrow">Data Security Alert</div>
    <h1>Factory Reset Is<br><span class="accent">Not Enough</span></h1>
    <p class="hero-sub">Your factory-reset phone still has all your data on it — photos, passwords, banking tokens. Anyone with $50 of software can get it back. Here's how to actually erase it.</p>
    <div>
      <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary">Erase Permanently — Free Trial</a>
      <a href="#how-it-works" class="btn-secondary">See How It Works</a>
    </div>
    <div class="hero-stats">
      <div class="stat"><span class="stat-num">1,000+</span><div class="stat-lbl">Supported Devices</div></div>
      <div class="stat"><span class="stat-num">3</span><div class="stat-lbl">Security Levels</div></div>
      <div class="stat"><span class="stat-num">DoD</span><div class="stat-lbl">5220.22-M Standard</div></div>
      <div class="stat"><span class="stat-num">PDF</span><div class="stat-lbl">Erasure Certificate</div></div>
    </div>
  </div>
</section>

<section class="danger-section">
  <div class="container">
    <div class="section-eyebrow">Why Factory Reset Fails</div>
    <h2>What You Don't Know About Your "Wiped" Phone</h2>
    <p class="section-lead">Factory reset removes the file directory — not the files. Cambridge University researchers recovered full data from factory-reset phones. Here's what that means for you.</p>
    <div class="danger-grid">{danger_cards}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-eyebrow">The Solution</div>
    <h2>What Dr.Fone Data Eraser Does Differently</h2>
    <p class="section-lead">Military-grade overwriting, erasure certificates, selective erase, and junk cleanup — in one tool for iPhone and Android.</p>
    <div class="features-grid">{feat_cards}</div>
  </div>
</section>

<section id="how-it-works" style="background:var(--bg2);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
  <div class="container">
    <div class="section-eyebrow">Process</div>
    <h2>How It Works — 4 Steps</h2>
    <p class="section-lead">Connect, choose, erase, and download your report. The entire process takes 15-90 minutes depending on security level chosen.</p>
    <div class="steps">{steps_html}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-eyebrow">Comparison</div>
    <h2>Dr.Fone vs Factory Reset vs Alternatives</h2>
    <p class="section-lead">See exactly what each method does — and doesn't — do to protect your data.</p>
    {COMPARISON_TABLE}
  </div>
</section>

<section style="background:var(--bg2);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
  <div class="container">
    <div class="section-eyebrow">Browse by Topic</div>
    <h2>All Categories ({len(cats_by)} Topics, {len(KEYWORDS)} Guides)</h2>
    <div class="blog-grid">{cat_cards}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-eyebrow">Research &amp; Guides</div>
    <h2>Latest from the Blog</h2>
    <div class="blog-grid">{blog_preview}</div>
    <div style="text-align:center;margin-top:32px"><a href="{BASE_PATH}/blog/" class="btn-secondary">All Blog Posts →</a></div>
  </div>
</section>

<section style="background:var(--bg2);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
  <div class="container">
    <div class="section-eyebrow">FAQ</div>
    <h2>Common Questions</h2>
    <div class="faq-list">{faq_html}</div>
    <div style="margin-top:24px"><a href="{BASE_PATH}/faq/">See all {len(FAQ_ITEMS)} questions →</a></div>
  </div>
</section>

<div class="cta-band">
  <div class="container">
    <div class="section-eyebrow">Get Protected</div>
    <h2>Erase Your Phone. Get Your Report. Done.</h2>
    <p>Permanently wipe iPhone and Android data with DoD-standard overwriting and a PDF certificate proving it's gone.</p>
    <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary">Download Dr.Fone Data Eraser Free</a>
    <div class="badges">
      <span class="badge">DoD 5220.22-M</span>
      <span class="badge">GDPR Compliant</span>
      <span class="badge">HIPAA</span>
      <span class="badge">ISO 27001</span>
      <span class="badge">PCI DSS</span>
      <span class="badge">Windows &amp; Mac</span>
      <span class="badge">iOS 7+</span>
      <span class="badge">Android 4.0+</span>
    </div>
  </div>
</div>"""

    return page(
        "DataEraserOnline — Factory Reset Is Not Enough | Permanently Erase Phone Data",
        "Factory reset leaves your data recoverable. Learn how to permanently erase iPhone and Android data using DoD-standard overwriting with an erasure certificate.",
        SITE_DOMAIN + "/",
        body, schema
    )

def kw_page(kwd):
    slug = kwd["slug"]; keyword = kwd["keyword"]; cat = kwd["cat"]
    cat_name = cat.replace("-"," ").title()
    title_page = f"{keyword} — Complete 2025 Guide"
    desc = f"How to {keyword.lower()} permanently with DoD-standard overwriting and an erasure certificate. Step-by-step guide with free trial."
    canonical = f"{SITE_DOMAIN}/keyword/{slug}/"

    breadcrumb_schema = json.dumps({
        "@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":SITE_DOMAIN},
            {"@type":"ListItem","position":2,"name":cat_name,"item":f"{SITE_DOMAIN}/category/{cat}/"},
            {"@type":"ListItem","position":3,"name":keyword,"item":canonical},
        ]
    })
    faq_schema = json.dumps({
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":f"Does factory reset permanently {keyword.lower()}?",
             "acceptedAnswer":{"@type":"Answer","text":"No. Factory reset removes the file directory but leaves data on storage, recoverable by recovery software. Use DoD-standard overwriting with Dr.Fone Data Eraser."}},
            {"@type":"Question","name":f"How long does it take to {keyword.lower()}?",
             "acceptedAnswer":{"@type":"Answer","text":"10-20 minutes (single pass), 25-45 minutes (DoD standard), 60-90 minutes (7-pass military). Depends on storage size and security level."}},
        ]
    })

    related = [k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    related_links = "".join(f'<li><a href="{BASE_PATH}/keyword/{k["slug"]}/">{k["keyword"]}</a></li>' for k in related)
    faq_html = "".join(f'<div class="faq-item"><div class="faq-q">{q}<span class="faq-toggle">+</span></div><div class="faq-a">{a}</div></div>' for q,a in FAQ_ITEMS[:4])

    body = f"""
<div class="breadcrumb">
  <div style="max-width:var(--max);margin:0 auto">
    <a href="{BASE_PATH}/">Home</a> › <a href="{BASE_PATH}/category/{cat}/">{cat_name}</a> › {keyword}
  </div>
</div>
<div class="kw-hero">
  <div class="container">
    <div class="section-eyebrow">{cat_name}</div>
    <h1>{keyword} — 2025 Complete Guide</h1>
    <p>Learn the only reliable way to permanently erase your data using DoD-standard overwriting — not just factory reset — with a PDF certificate proving it's gone.</p>
  </div>
</div>
<div class="kw-body">
  <h2>Why Factory Reset Is Not Enough for {keyword}</h2>
  <p>When you factory reset your device, the operating system removes the file directory — the index that tells it where your files live. But the files themselves remain on the NAND flash storage, intact and recoverable with freely available software.</p>
  <p>For a task as sensitive as <strong>{keyword.lower()}</strong>, factory reset alone leaves you exposed. Data recovery tools that cost under $50 can reconstruct your photos, messages, contacts, and banking app tokens from a factory-reset device.</p>

  <h2>The Right Way to {keyword}</h2>
  <ol>
    <li><strong>Download Dr.Fone Data Eraser</strong> — available for Windows and Mac</li>
    <li><strong>Connect your device</strong> via USB cable</li>
    <li><strong>Choose your security level</strong> — Level 2 (DoD 3-pass) recommended for most users</li>
    <li><strong>Run the erase</strong> — takes 20-45 minutes depending on storage size</li>
    <li><strong>Download your erasure report PDF</strong> — includes IMEI, timestamp, security level</li>
    <li><strong>Factory reset as a final step</strong> to restore the OS to out-of-box state</li>
  </ol>

  <h2>Three Security Levels</h2>
  <p><strong>Level 1 — Single Pass:</strong> One overwrite of pseudorandom data. Sufficient for giving a device to a trusted family member. Fast (10-20 min).</p>
  <p><strong>Level 2 — DoD Standard:</strong> Three overwrite passes following DoD 5220.22-M. Recommended for selling online or trade-in programs. (25-45 min).</p>
  <p><strong>Level 3 — Military:</strong> Seven passes plus cryptographic key destruction. Required for corporate compliance with GDPR, HIPAA, PCI DSS. (60-90 min).</p>

  <h2>Supported Devices</h2>
  <p>Dr.Fone Data Eraser supports all iPhone and iPad models running iOS 7 and above, plus all major Android devices — Samsung Galaxy, Google Pixel, Xiaomi, OPPO, Vivo, Motorola, LG, and 1,000+ more models.</p>

  <div style="background:rgba(220,38,38,.07);border:1px solid rgba(220,38,38,.2);border-radius:8px;padding:24px;margin:32px 0;text-align:center">
    <p style="font-weight:700;margin-bottom:12px">Ready to {keyword.lower()} permanently?</p>
    <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary">Download Dr.Fone Data Eraser — Free Trial</a>
  </div>

  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">{faq_html}</div>

  {f'<h2>Related: {cat_name} Guides</h2><ul>{related_links}</ul>' if related else ''}
</div>"""

    schema = breadcrumb_schema[:-1] + "," + faq_schema[1:]  # Merge two schemas
    return page(title_page, desc, canonical, body, breadcrumb_schema)

def category_page(cat, kws):
    cat_name = cat.replace("-"," ").title()
    title_page = f"{cat_name} — {len(kws)} Guides | DataEraserOnline"
    desc = f"All {cat_name.lower()} guides in one place. {len(kws)} keyword articles covering every angle of {cat_name.lower()}."
    canonical = f"{SITE_DOMAIN}/category/{cat}/"
    kw_cards = "".join(f'<div class="blog-card"><h3><a href="{BASE_PATH}/keyword/{k["slug"]}/">{k["keyword"]}</a></h3><p>Complete 2025 guide to {k["keyword"].lower()} using DoD-standard overwriting.</p></div>' for k in kws)
    body = f"""
<div class="kw-hero">
  <div class="container">
    <div class="section-eyebrow">Category</div>
    <h1>{cat_name}</h1>
    <p>{len(kws)} in-depth guides covering every aspect of {cat_name.lower()}. All methods use DoD-standard overwriting — not just factory reset.</p>
  </div>
</div>
<div class="container" style="padding:48px 24px">
  <div class="blog-grid">{kw_cards}</div>
  <div style="text-align:center;margin-top:48px">
    <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary">Download Dr.Fone Data Eraser — Free Trial</a>
  </div>
</div>"""
    return page(title_page, desc, canonical, body)

def blog_index():
    cards = "".join(f'<div class="blog-card"><div class="blog-cat">Data Security</div><h3><a href="{BASE_PATH}/blog/{b["slug"]}/">{b["title"]}</a></h3><p>{b["desc"]}</p><div class="blog-date">{b["date"]}</div></div>' for b in BLOG_POSTS)
    body = f"""
<div class="kw-hero"><div class="container"><h1>Data Security Blog</h1><p>{len(BLOG_POSTS)} research-backed articles on phone data erasure, privacy, and compliance.</p></div></div>
<div class="container" style="padding:48px 24px"><div class="blog-grid">{cards}</div></div>"""
    return page("Data Erasure Blog — Research & Guides | DataEraserOnline","Research-backed articles on phone data erasure, privacy protection, and compliance.",f"{SITE_DOMAIN}/blog/",body)

def blog_post_page(b):
    schema = json.dumps({
        "@context":"https://schema.org","@type":"BlogPosting",
        "headline":b["title"],"description":b["desc"],
        "datePublished":b["date"],"dateModified":b["date"],
        "author":{"@type":"Organization","name":"DataEraserOnline"},
        "publisher":{"@type":"Organization","name":"DataEraserOnline","url":SITE_DOMAIN},
        "url":f"{SITE_DOMAIN}/blog/{b['slug']}/",
        "mainEntityOfPage":{"@type":"WebPage","@id":f"{SITE_DOMAIN}/blog/{b['slug']}/"},
    })
    body = f"""
<div class="breadcrumb"><div style="max-width:var(--max);margin:0 auto"><a href="{BASE_PATH}/">Home</a> › <a href="{BASE_PATH}/blog/">Blog</a> › {b["title"]}</div></div>
<div class="post-hero"><div class="section-eyebrow">Data Security Research</div><h1>{b["title"]}</h1><div class="post-meta">Published {b["date"]} · DataEraserOnline</div></div>
<article class="post-body">
{b["content"]}
<div class="post-cta">
  <p>Ready to permanently erase your phone data? Dr.Fone Data Eraser uses DoD-standard overwriting — not just factory reset — and generates a PDF erasure certificate.</p>
  <a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary">Download Free Trial →</a>
</div>
</article>"""
    return page(f"{b['title']} | DataEraserOnline", b["desc"], f"{SITE_DOMAIN}/blog/{b['slug']}/", body, schema, "article")

def faq_page():
    all_faqs = "".join(f'<div class="faq-item"><div class="faq-q">{q}<span class="faq-toggle">+</span></div><div class="faq-a">{a}</div></div>' for q,a in FAQ_ITEMS)
    body = f"""
<div class="kw-hero"><div class="container"><h1>FAQ — Data Erasure Questions</h1><p>Everything you need to know about permanently erasing phone and PC data.</p></div></div>
<div class="container" style="padding:48px 24px"><div class="faq-list">{all_faqs}</div></div>"""
    return page("FAQ — Data Erasure Questions | DataEraserOnline","Answers to the most common questions about permanently erasing phone data before selling.",f"{SITE_DOMAIN}/faq/",body)

def glossary_page():
    items = "".join(f'<div class="gloss-item"><div class="gloss-term">{t}</div><div class="gloss-def">{d}</div></div>' for t,d in GLOSSARY_TERMS)
    body = f"""
<div class="kw-hero"><div class="container"><h1>Data Erasure Glossary</h1><p>{len(GLOSSARY_TERMS)} key terms every phone seller and IT manager should know.</p></div></div>
<div class="container" style="padding:48px 24px"><div class="glossary-grid">{items}</div></div>"""
    return page(f"Data Erasure Glossary — {len(GLOSSARY_TERMS)} Terms | DataEraserOnline","Definitions of key data security, erasure, and compliance terms.",f"{SITE_DOMAIN}/glossary/",body)

def categories_page():
    cats_by = defaultdict(list)
    for kwd in KEYWORDS: cats_by[kwd["cat"]].append(kwd)
    cards = "".join(f'<div class="blog-card"><div class="blog-cat">{len(kws)} guides</div><h3><a href="{BASE_PATH}/category/{cat}/">{cat.replace("-"," ").title()}</a></h3><p>Browse all guides on {cat.replace("-"," ").lower()}.</p></div>' for cat,kws in sorted(cats_by.items()))
    body = f"""
<div class="kw-hero"><div class="container"><h1>All Categories ({len(cats_by)} Topics)</h1><p>Browse {len(KEYWORDS)} keyword guides across {len(cats_by)} categories.</p></div></div>
<div class="container" style="padding:48px 24px"><div class="blog-grid">{cards}</div></div>"""
    return page("All Categories | DataEraserOnline",f"Browse {len(KEYWORDS)} data erasure guides across {len(cats_by)} topics.",f"{SITE_DOMAIN}/categories/",body)

def about_page():
    body = f"""
<div class="kw-hero"><div class="container"><h1>About DataEraserOnline</h1></div></div>
<div class="post-body">
<p>DataEraserOnline is an independent review and guide site focused on phone and PC data security. Our mission is simple: help people understand that factory reset is not enough — and give them the information they need to protect themselves before selling, donating, or recycling devices.</p>
<h2>Who We Are</h2>
<p>We're a team of privacy researchers and tech writers who've seen too many identity theft cases trace back to improperly wiped devices. We built this site to be the most comprehensive, honest resource on phone data erasure on the internet.</p>
<h2>Affiliate Disclosure</h2>
<p>DataEraserOnline is affiliated with Wondershare Dr.Fone Data Eraser. We earn a commission when you purchase through our links at no additional cost to you. This does not affect our editorial independence — we recommend Dr.Fone because we've evaluated it against alternatives and believe it's the best tool for the job.</p>
<h2>Contact</h2>
<p>Questions, corrections, or partnership inquiries: use our <a href="{BASE_PATH}/contact/">contact page</a>.</p>
</div>"""
    return page("About | DataEraserOnline","About DataEraserOnline — independent review site for phone data erasure tools and privacy guides.",f"{SITE_DOMAIN}/about/",body)

def contact_page():
    body = f"""
<div class="kw-hero"><div class="container"><h1>Contact</h1></div></div>
<div class="post-body">
<p>For questions, corrections, or partnership inquiries, email us at: <strong>contact [at] dataeraseronline.com</strong></p>
<p>We aim to respond within 2 business days.</p>
</div>"""
    return page("Contact | DataEraserOnline","Contact the DataEraserOnline team.",f"{SITE_DOMAIN}/contact/",body)

def privacy_page():
    body = f"""
<div class="kw-hero"><div class="container"><h1>Privacy Policy</h1></div></div>
<div class="post-body">
<p>Last updated: {BUILD_DATE}</p>
<h2>Information We Collect</h2>
<p>This site uses standard web analytics (page views, referral sources) and does not collect personally identifiable information beyond what you voluntarily provide via our contact form.</p>
<h2>Cookies</h2>
<p>We use essential cookies for site functionality. Analytics cookies collect anonymized usage data. You may disable cookies in your browser settings.</p>
<h2>Affiliate Links</h2>
<p>This site contains affiliate links to Wondershare Dr.Fone. When you click these links and make a purchase, we earn a commission at no cost to you. The tracking is handled by LinkConnector.</p>
<h2>Third-Party Services</h2>
<p>Google Fonts is loaded from Google's CDN. Google Analytics may be used for traffic analysis. Both are subject to their respective privacy policies.</p>
<h2>Contact</h2>
<p>Privacy questions: <a href="{BASE_PATH}/contact/">contact page</a>.</p>
</div>"""
    return page("Privacy Policy | DataEraserOnline","Privacy policy for DataEraserOnline.",f"{SITE_DOMAIN}/privacy/",body)

def terms_page():
    body = f"""
<div class="kw-hero"><div class="container"><h1>Terms of Use</h1></div></div>
<div class="post-body">
<p>Last updated: {BUILD_DATE}</p>
<h2>Informational Content Only</h2>
<p>Content on this site is for informational purposes only. We make no warranties about the accuracy, completeness, or fitness for purpose of any information provided.</p>
<h2>Affiliate Relationship</h2>
<p>This site participates in the Wondershare affiliate program. See our affiliate disclosure in the Privacy Policy.</p>
<h2>Limitation of Liability</h2>
<p>DataEraserOnline is not liable for any data loss, security incidents, or damages arising from use of or reliance on information provided on this site.</p>
<h2>Governing Law</h2>
<p>These terms are governed by applicable law in the jurisdiction of the site operator.</p>
</div>"""
    return page("Terms of Use | DataEraserOnline","Terms of use for DataEraserOnline.",f"{SITE_DOMAIN}/terms/",body)

def download_page():
    body = f"""
<div class="kw-hero"><div class="container"><h1>Download Dr.Fone Data Eraser</h1><p>Free trial available for Windows and Mac. Supports all iPhone, iPad, and Android devices.</p></div></div>
<div class="container" style="padding:48px 24px;text-align:center">
<p style="color:var(--muted);margin-bottom:32px;max-width:580px;margin-left:auto;margin-right:auto">Click below to go to the official Wondershare download page. The free trial lets you scan your device and preview what will be erased before committing to a purchase.</p>
<a href="{AFFILIATE_URL}" target="_blank" rel="noopener" class="btn-primary" style="font-size:1.1rem;padding:18px 48px">Download Dr.Fone Data Eraser — Free Trial</a>
<div class="badges" style="margin-top:32px">
  <span class="badge">Windows 7/8/10/11</span><span class="badge">macOS 10.10+</span>
  <span class="badge">iOS 7+</span><span class="badge">Android 4.0+</span>
  <span class="badge">No Root/Jailbreak</span><span class="badge">1,000+ Devices</span>
</div>
</div>"""
    return page("Download Dr.Fone Data Eraser — Free Trial | DataEraserOnline","Download Dr.Fone Data Eraser free trial for Windows and Mac. Permanently erase iPhone and Android data.",f"{SITE_DOMAIN}/download/",body)

# ═══════════════════════════════════════════════════════════════
#  SITEMAP + LLMS.TXT + ROBOTS
# ═══════════════════════════════════════════════════════════════
def sitemap(all_urls):
    urls = "\n".join(f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>" for u in all_urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

def llms_txt():
    cats_by = defaultdict(list)
    for kwd in KEYWORDS: cats_by[kwd["cat"]].append(kwd)
    sample = ", ".join(k["keyword"] for k in KEYWORDS[:20])
    cats = list(cats_by.keys())
    return (
        f"# DataEraserOnline\n\n"
        f"> Comprehensive guide to permanently erasing iPhone and Android data. "
        f"Core message: factory reset is not enough — it removes the file directory but leaves data on NAND storage, "
        f"recoverable by anyone with $50 of recovery software.\n\n"
        f"## Product\nWondershare Dr.Fone Data Eraser — military-grade DoD 5220.22-M overwrite, "
        f"3 security levels, erasure report PDF with IMEI, selective erase, junk cleanup, 1,000+ iOS and Android devices.\n\n"
        f"## Compliance\nGDPR Article 17 · HIPAA PHI · ISO 27001 · NIST 800-88 · PCI DSS\n\n"
        f"## Platforms\nWindows 7/8/10/11 · macOS 10.10+ · iOS 7+ · Android 4.0+\n\n"
        f"## Download\n{AFFILIATE_URL}\n\n"
        f"## Site\n{SITE_DOMAIN}\n"
        f"{len(KEYWORDS)} keyword pages · {len(BLOG_POSTS)} blog posts · {len(cats)} categories\n"
        f"Sitemap: {SITE_DOMAIN}/sitemap.xml\n\n"
        f"## Categories\n{', '.join(c.title() for c in cats)}\n\n"
        f"## Sample Keywords\n{sample}\n"
    )

def robots():
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_DOMAIN}/sitemap.xml\n"

# ═══════════════════════════════════════════════════════════════
#  BUILD
# ═══════════════════════════════════════════════════════════════
def write(path, content):
    p = DIST / path
    p.parent.mkdir(parents=True, exist_ok=True)
    mode = "wb" if isinstance(content, bytes) else "w"
    enc = {} if isinstance(content, bytes) else {"encoding": "utf-8"}
    with open(p, mode, **enc) as f:
        f.write(content)

def progress(i, total, label=""):
    pct = i / total
    bar = "█" * int(30 * pct) + "░" * (30 - int(30 * pct))
    print(f"\r[{bar}] {i}/{total} {label:<40}", end="", flush=True)

if __name__ == "__main__":
    import shutil
    if DIST.exists(): shutil.rmtree(DIST)
    DIST.mkdir()

    all_urls = []
    file_count = 0

    # Homepage
    write("index.html", homepage())
    all_urls.append(SITE_DOMAIN + "/")
    file_count += 1
    print(f"✓ Homepage")

    # Essential pages
    essentials = {
        "blog/index.html": blog_index(),
        "faq/index.html": faq_page(),
        "glossary/index.html": glossary_page(),
        "categories/index.html": categories_page(),
        "about/index.html": about_page(),
        "contact/index.html": contact_page(),
        "privacy/index.html": privacy_page(),
        "terms/index.html": terms_page(),
        "download/index.html": download_page(),
    }
    for path, content in essentials.items():
        write(path, content)
        slug = path.replace("/index.html","")
        all_urls.append(f"{SITE_DOMAIN}/{slug}/")
        file_count += 1
    print(f"✓ Essential pages ({len(essentials)})")

    # Blog posts
    for i, b in enumerate(BLOG_POSTS):
        write(f"blog/{b['slug']}/index.html", blog_post_page(b))
        all_urls.append(f"{SITE_DOMAIN}/blog/{b['slug']}/")
        file_count += 1
        progress(i+1, len(BLOG_POSTS), f"Blog: {b['slug'][:30]}")
    print(f"\n✓ Blog posts ({len(BLOG_POSTS)})")

    # Keyword pages
    for i, kwd in enumerate(KEYWORDS):
        write(f"keyword/{kwd['slug']}/index.html", kw_page(kwd))
        all_urls.append(f"{SITE_DOMAIN}/keyword/{kwd['slug']}/")
        file_count += 1
        progress(i+1, len(KEYWORDS), kwd["slug"][:35])
    print(f"\n✓ Keyword pages ({len(KEYWORDS)})")

    # Category pages
    cats_by = defaultdict(list)
    for kwd in KEYWORDS: cats_by[kwd["cat"]].append(kwd)
    for i, (cat, kws) in enumerate(cats_by.items()):
        write(f"category/{cat}/index.html", category_page(cat, kws))
        all_urls.append(f"{SITE_DOMAIN}/category/{cat}/")
        file_count += 1
        progress(i+1, len(cats_by), cat)
    print(f"\n✓ Category pages ({len(cats_by)})")

    # Static files
    write("sitemap.xml", sitemap(all_urls))
    write("llms.txt", llms_txt())
    write("robots.txt", robots())
    write("404.html", page("404 — Page Not Found | DataEraserOnline","Page not found.",SITE_DOMAIN+"/404.html",
        f'<div class="kw-hero"><div class="container"><h1>404 — Page Not Found</h1><p><a href="{BASE_PATH}/">← Back to home</a></p></div></div>'))
    file_count += 4

    print(f"\n{'='*50}")
    print(f"BUILD COMPLETE")
    print(f"  Files        : {file_count:,}")
    print(f"  Keywords     : {len(KEYWORDS)}")
    print(f"  Blog posts   : {len(BLOG_POSTS)}")
    print(f"  Categories   : {len(cats_by)}")
    print(f"  All URLs     : {len(all_urls)}")
    print(f"  Output       : {DIST}/")
    size = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file())
    print(f"  Total size   : {size/1024/1024:.1f} MB")
    print(f"  Live at      : {SITE_DOMAIN}/")
