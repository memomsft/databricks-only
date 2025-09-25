# 05 – Publish the Bot to Microsoft Teams

This guide explains how to package your Azure Bot as a **Teams app**, upload it via **Developer Portal**, and verify it works end-to-end with your Databricks Genie backend. 

---

## 5.1 Requirements (Teams & Tenant)

- A **Microsoft 365 tenant** where we can upload custom apps. We are using a Contoso Tenant (special) for this purpose 
- **Teams custom app upload** must be allowed. In **Teams admin center**:  
  `Teams apps → Setup policies → Upload custom apps = On`

  
- You can upload apps via **Teams client** (`Apps → Manage your apps → Upload an app → Upload a custom app`) or through **Developer Portal** (“Import app”, “Publish to org”). :contentReference[oaicite:3]{index=3}
- Note for government clouds: custom-app upload is available in **GCC**, but **not** in GCC High/DoD or Teams operated by 21Vianet. :contentReference[oaicite:4]{index=4}

**We’ll need from previous sections**
- **Microsoft App ID** (Azure Bot’s App ID).
- **Messaging endpoint** (your Web App `/api/messages`).
- Optional: **Genie Space ID / endpoint** (already wired in the backend).

---

## 5.2 Gather Assets

- **Bot App ID** (from Azure Bot → *Configuration*). :contentReference[oaicite:5]{index=5}  
- **Two icons** in PNG:
  - `color.png` (192×192, full-color)  
  - `outline.png` (32×32, transparent outline)  
  These are required for packaging and store readiness. :contentReference[oaicite:6]{index=6}
- **Valid domain** of your backend, e.g. `your-webapp.azurewebsites.net`, for `validDomains` in the manifest. :contentReference[oaicite:7]{index=7}

---

## 5.3 Create the Teams App Manifest

Create `manifest.json` in a folder with your two icons. This template targets **Teams** and supports **personal, team, and group chat** scopes.

> Replace all `<>` placeholders. If you aren’t using Bot **SSO**, you may omit `webApplicationInfo`. :contentReference[oaicite:8]{index=8}

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.13/MicrosoftTeams.schema.json",
  "manifestVersion": "1.13",
  "version": "1.0.0",
  "id": "<NEW-GUID-FOR-THIS-TEAMS-APP>",
  "packageName": "com.<yourorg>.genie",
  "developer": {
    "name": "<Your Organization>",
    "websiteUrl": "https://<your-domain>",
    "privacyUrl": "https://<your-domain>/privacy",
    "termsOfUseUrl": "https://<your-domain>/terms"
  },
  "name": {
    "short": "Genie Bot",
    "full": "Databricks Genie for Teams"
  },
  "description": {
    "short": "Ask data questions in natural language.",
    "full": "A Microsoft Teams bot that forwards your questions to Databricks Genie and returns answers from your Lakehouse."
  },
  "icons": {
    "color": "color.png",
    "outline": "outline.png"
  },
  "accentColor": "#FFFFFF",
  "bots": [
    {
      "botId": "<MICROSOFT_APP_ID_OF_YOUR_AZURE_BOT>",
      "scopes": [ "personal", "team", "groupchat" ],
      "supportsFiles": false,
      "isNotificationOnly": false,
      "commandLists": [
        {
          "scopes": [ "personal", "team", "groupchat" ],
          "commands": [
            { "title": "help", "description": "Show available commands" },
            { "title": "genie <question>", "description": "Send a question to Databricks Genie" }
          ]
        }
      ]
    }
  ],
  "webApplicationInfo": {
    "id": "<MICROSOFT_APP_ID_OF_YOUR_AZURE_BOT>",
    "resource": "api://botid-<MICROSOFT_APP_ID_OF_YOUR_AZURE_BOT>"
  },
  "validDomains": [
    "<your-webapp-name>.azurewebsites.net"
  ]
}

