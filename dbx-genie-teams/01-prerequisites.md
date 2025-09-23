# 2. Prerequisites

Before starting, make sure you have the following resources and permissions in place.

---

## 🟠 Databricks
- Access to a **Databricks workspace** (Premium or Enterprise edition recommended).  
- Sufficient **permissions** to install and configure **Databricks Genie** and read/write tables (typically Workspace Admin or equivalent will be enough for this exercise).  
- A running **cluster** or SQL warehouse that Genie can query.  

---

## 🔵 Azure
You’ll need an active **Azure Subscription** with the following resources:

- **App Service Plan** → to host the middleware service.  
- **Web App** → where the backend (Python/Node.js) will be deployed.  
- **Azure Bot resource** → to register and configure the Teams bot.  
- **Azure Active Directory App Registration** → for bot authentication and API permissions.  
- **Azure Key Vault** *(optional but recommended)* → to securely store Genie API keys, client secrets, and connection strings.  

---

## 🟣 Microsoft Teams
- **Developer permissions** in your Microsoft 365 tenant.  
- Ability to **upload and test a custom Teams App Manifest**. This requires access to Microsoft Teams Developer Portal 
- (Optional) A dedicated **Teams environment** for testing before deploying org-wide.  

---

⚡ With these prerequisites in place, you’ll be ready to set up the integration end-to-end.

