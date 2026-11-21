import streamlit as st

st.set_page_config(page_title="Free Trading Library", page_icon="📚", layout="wide")

st.title("📚 Free Trading & Investing Library")
st.caption("Legal, Free & Valuable Study Material (Hindi | English | Roman/Hinglish)")

# Language Filter
lang_filter = st.radio(
    "Language Filter Chunein:",
    ["All", "Hindi", "English", "Roman / Hinglish"],
    horizontal=True
)

# --- YAHAN NAYE LINKS ADD YA UPDATE KAREIN ---
RESOURCES = {
    "Indian": {
        "Stock Investing": [
            {
                "title": "Zerodha Varsity - Fundamental Analysis (Hindi)",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "Hindi",
                "desc": "Company balance sheet, P&L aur long-term investing seekhne ka best free module.",
                "url": "https://zerodha.com/varsity/hindi/"
            },
            {
                "title": "Zerodha Varsity - Fundamental Analysis (English)",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "English",
                "desc": "Complete step-by-step fundamental analysis guide with free PDFs.",
                "url": "https://zerodha.com/varsity/module/fundamental-analysis/"
            },
            {
                "title": "SEBI Investor Education Booklets",
                "author": "SEBI (Official)",
                "lang": "Hindi",
                "desc": "Share market ke basic rules aur investor safety par official free Hindi/English booklets.",
                "url": "https://investor.sebi.gov.in/"
            }
        ],
        "Intraday": [
            {
                "title": "Zerodha Varsity - Technical Analysis (English)",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "English",
                "desc": "Candlesticks, Support/Resistance, Indicators aur Chart Patterns ki puri jankari.",
                "url": "https://zerodha.com/varsity/module/technical-analysis/"
            },
            {
                "title": "Price Action & Intraday Basics (Hinglish Videos)",
                "author": "Indian Market Educators (YouTube)",
                "lang": "Roman / Hinglish",
                "desc": "Intraday trading, VWAP aur price action setups Hinglish mein.",
                "url": "https://www.youtube.com/results?search_query=intraday+price+action+trading+course+hindi"
            }
        ],
        "Options": [
            {
                "title": "Zerodha Varsity - Option Theory for Professional Trading",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "English",
                "desc": "Option Greeks (Delta, Gamma, Theta, Vega) aur volatility ko gehrai se samajhne ke liye.",
                "url": "https://zerodha.com/varsity/module/option-theory/"
            },
            {
                "title": "Zerodha Varsity - Option Strategies",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "English",
                "desc": "Bull Call Spread, Iron Condor, Straddle aur hedging strategies.",
                "url": "https://zerodha.com/varsity/module/option-strategies/"
            },
            {
                "title": "NSE India - Derivatives & Options Learning",
                "author": "NSE Official",
                "lang": "English",
                "desc": "NSE ki taraf se official F&O aur market structure study material.",
                "url": "https://www.nseindia.com/learn"
            }
        ],
        "Forex": [
            {
                "title": "Zerodha Varsity - Currency & Commodity Markets",
                "author": "Karthik Rangappa (Zerodha)",
                "lang": "English",
                "desc": "Indian regulated currency pairs (USDINR, EURINR) aur forex mechanics.",
                "url": "https://zerodha.com/varsity/module/commodities-currency-government-securities/"
            }
        ]
    },
    "Foreign": {
        "Stock Investing": [
            {
                "title": "The Intelligent Investor (Hindi Summary / Audiobook)",
                "author": "Benjamin Graham",
                "lang": "Roman / Hinglish",
                "desc": "Value investing ki sabse mashhoor kitab ka free Hindi/Hinglish summary.",
                "url": "https://www.youtube.com/results?search_query=The+Intelligent+Investor+Hindi+Audiobook+Summary"
            },
            {
                "title": "Extraordinary Popular Delusions (Free Public Domain Book)",
                "author": "Charles Mackay",
                "lang": "English",
                "desc": "Market bubbles aur crowd psychology par classic free eBook (Project Gutenberg).",
                "url": "https://www.gutenberg.org/ebooks/24518"
            }
        ],
        "Intraday": [
            {
                "title": "Reminiscences of a Stock Operator (Free Public Domain)",
                "author": "Edwin Lefèvre (Jesse Livermore)",
                "lang": "English",
                "desc": "Trading psychology aur tape reading par duniya ki sabse classic kitab (Internet Archive).",
                "url": "https://archive.org/details/reminiscencesofs00lefe"
            },
            {
                "title": "Studies in Tape Reading (Free Public Domain)",
                "author": "Richard D. Wyckoff",
                "lang": "English",
                "desc": "Smart Money aur Volume/Price analysis (Wyckoff Method) ki original book.",
                "url": "https://archive.org/details/studiesintaperea00wyck"
            },
            {
                "title": "Trading in the Zone (Hindi Summary / Audiobook)",
                "author": "Mark Douglas",
                "lang": "Roman / Hinglish",
                "desc": "Trading discipline, FOMO aur fear par kaabu paane ke liye best psychology book.",
                "url": "https://www.youtube.com/results?search_query=Trading+in+the+Zone+Mark+Douglas+Hindi+Summary"
            },
            {
                "title": "Japanese Candlestick Charting Techniques (Hindi Summary)",
                "author": "Steve Nison",
                "lang": "Hindi",
                "desc": "Candlestick patterns ki shuruat aur asli logic samajhne ke liye.",
                "url": "https://www.youtube.com/results?search_query=Japanese+Candlestick+Charting+Techniques+Steve+Nison+Hindi"
            }
        ],
        "Options": [
            {
                "title": "Option Volatility & Pricing (Hindi/English Breakdown)",
                "author": "Sheldon Natenberg",
                "lang": "Roman / Hinglish",
                "desc": "Professional options pricing aur implied volatility (IV) par top foreign book summary.",
                "url": "https://www.youtube.com/results?search_query=Option+Volatility+and+Pricing+Sheldon+Natenberg+Summary"
            }
        ],
        "Forex": [
            {
                "title": "BabyPips - School of Pipsology (100% Free Course)",
                "author": "BabyPips (Foreign)",
                "lang": "English",
                "desc": "Forex trading seekhne ke liye duniya ka sabse popular aur free structured course.",
                "url": "https://www.babypips.com/learn/forex"
            },
            {
                "title": "IFC Markets - Free Forex eBooks (Hindi & English)",
                "author": "IFC Markets",
                "lang": "Hindi",
                "desc": "Beginners ke liye muft Forex trading PDF eBooks aur tutorials.",
                "url": "https://www.ifcmarkets.com/en/forex-books"
            }
        ]
    }
}

def display_section(author_type):
    categories = ["Stock Investing", "Intraday", "Options", "Forex"]
    for cat in categories:
        items = RESOURCES[author_type].get(cat, [])
        if lang_filter != "All":
            items = [item for item in items if item["lang"] == lang_filter]
        
        with st.expander(f"📂 {cat} ({len(items)} Resources)", expanded=True):
            if not items:
                st.info(f"Is category mein '{lang_filter}' language ka koi resource abhi add nahi hai.")
            else:
                for item in items:
                    st.markdown(f"**📖 {item['title']}**")
                    st.markdown(f"*Author:* {item['author']} | *Language:* `{item['lang']}`")
                    st.write(item['desc'])
                    st.link_button("🔗 Open Free Resource", item['url'])
                    st.divider()

tab1, tab2 = st.tabs(["🇮🇳 Indian Authors & Platforms", "🌍 Foreign Authors & Classics"])

with tab1:
    display_section("Indian")

with tab2:
    display_section("Foreign")

st.warning(
    "⚠️ **Educational Disclaimer:** Ye saare links sirf learning aur educational purpose ke liye hain. "
    "Bharat mein bina RBI/SEBI ki anumati ke unauthorized foreign forex platforms par trade karna legal nahi hai."
)
