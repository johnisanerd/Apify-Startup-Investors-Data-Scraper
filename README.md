# 💰 Startup Investors API: VC and Investor Firm Data in Clean JSON

> The efficient, reliable, and developer-friendly way to use the Startup Investors API.

**Actor page:** [apify.com/johnvc/startup-investors-data-scraper](https://apify.com/johnvc/startup-investors-data-scraper?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/startup-investors-data-scraper/input-schema](https://apify.com/johnvc/startup-investors-data-scraper/input-schema?fpr=9n7kx3)

The Startup Investors API searches a curated database of over 10,000 investor firms, including venture capital, angel, accelerator, private equity, and family-office investors. Filter by firm type, focus industry, investment stage, country, or a free-text keyword, then optionally pull verified investor contacts (partners and principals) at each firm. Results come back as clean, structured JSON, ready for prospecting, fundraising research, or market analysis.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Startup-Investors-Data-Scraper.git
   cd Apify-Startup-Investors-Data-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python fetch-startup-investors-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python fetch-startup-investors-scraper.py
```

## Why Use This Startup Investors API?

**A curated investor database.** Over 10,000 investor firms across venture capital, angel, accelerator, private equity, and family-office categories, in one structured source.

**Precise filtering.** Narrow by firm type, focus industry, investment stage, and country, or run a free-text keyword search across firm names, descriptions, and theses.

**Verified contacts on demand.** Enable `Include_Contacts` to add an `investor_contacts` array to every firm, with each contact's name, job title, email (when available), and LinkedIn URL.

**Pagination built in.** Combine `Max_Results` and `Offset` to page through large result sets across runs, and `Order_By` for stable ordering.

**Predictable, pay-per-use pricing.** Billing is per firm returned, plus a per-contact fee when contacts are enabled, with a small per-run start fee and no subscription. Use filters and a low `Max_Results` to control cost.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can pull investor data for you on demand.

## Features

### Core Capabilities
- **Firm-type filtering** across venture capital, angel, accelerator, private equity, family office, and more
- **Industry focus filtering** by target sector
- **Investment-stage filtering** from pre-seed through growth
- **Country filtering** by headquarters location
- **Keyword search** across firm names, descriptions, and theses
- **Optional investor contacts** with name, title, email, and LinkedIn

### Data Quality
- **Structured firm records** with a stable field set
- **Profile links** including firm website and social profiles
- **Stage and focus arrays** for each firm
- **Search metadata** echoed on every record
- **Pagination support** with `Max_Results` and `Offset`

## Usage Examples

### Keyword search, small result set
```json
{
  "Keyword": "Sequoia",
  "Max_Results": 5
}
```

### Filter by type, focus, stage, and country
```json
{
  "Firm_Types": ["Venture Capital Investor", "Angel Investor"],
  "Focus_Areas": ["Artificial Intelligence"],
  "Investment_Stages": ["Seed", "Series A"],
  "Countries": ["United States"],
  "Max_Results": 25,
  "Include_Contacts": true
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `Firm_Types` | `array` | No | - | Investor firm types, e.g. `Venture Capital Investor`, `Angel Investor`, `Accelerator`. |
| `Focus_Areas` | `array` | No | - | Target industries, e.g. `Artificial Intelligence`, `Biotechnology`. |
| `Investment_Stages` | `array` | No | - | Stages, e.g. `Pre-Seed`, `Seed`, `Series A`. |
| `Countries` | `array` | No | - | Headquarters countries (full English names), e.g. `United States`. |
| `Keyword` | `string` | No | - | Free-text search across firm names, descriptions, and theses. |
| `Max_Results` | `integer` | No | `100` | Maximum firms to return (1-10000). Each firm is billed; keep this low and use filters to control cost. |
| `Offset` | `integer` | No | `0` | Skip this many firms before returning; combine with `Max_Results` to paginate. |
| `Order_By` | `string` | No | `created_at` | Sort field: `created_at`, `firm_name`, `firm_country`, or `firm_type_id`. |
| `Order_Direction` | `string` | No | `desc` | Sort direction: `asc` or `desc`. |
| `Include_Contacts` | `boolean` | No | `false` | Add an `investor_contacts` array to each firm. Billed per contact. |

## Output Format

A real result for the keyword `Sequoia` (one item per firm; reference profile fields and timestamps are present but trimmed here for readability).

```json
{
  "firm_id": 3466,
  "firm_type_id": "VC",
  "firm_name": "AI Fund",
  "firm_city": "Palo Alto",
  "firm_state": "California",
  "firm_country": "United States",
  "firm_zip": "94306",
  "firm_website": "https://aifund.ai/",
  "firm_linkedin_url": "https://www.linkedin.com/company/aifund",
  "twitter_url": "https://www.twitter.com/ai_fund",
  "firm_description": "AI Fund is a VC firm made up of AI pioneers, operators, entrepreneurs, and investors, supported by LPs such as NEA, Sequoia and Greylock.",
  "firm_stages": ["Pre-Seed", "Seed"],
  "firm_focus": ["Software & Internet", "Information Technology"],
  "firm_aum": 0,
  "last_checked": "2025-05-03T08:14:46Z",
  "created_at": "2025-06-12T07:14:44Z",
  "updated_at": "2025-06-12T07:14:44Z",
  "search_metadata": {
    "keyword": "Sequoia",
    "max_results": 3,
    "total_results_found": 3,
    "include_contacts": false
  }
}
```

Each firm record also includes additional reference and profile fields. When `Include_Contacts` is `true`, every firm gains an `investor_contacts` array, where each contact carries name, job title, email (when available), and LinkedIn URL.

---

## Use as an MCP tool

You can load the Startup Investors API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Startup Investors API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Startup Investors API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Startup Investors API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/startup-investors-data-scraper`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper`, using OAuth when prompted.
5. Ask Claude to run the Startup Investors API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Startup Investors API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/startup-investors-data-scraper`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Startup Investors API to power fundraising research, investor prospecting, and market analysis with reliable, structured data.*

Last Updated: 2026.06.14
