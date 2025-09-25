# 05 – Publish the Bot to Microsoft Teams

This guide explains how to package your Azure Bot as a **Teams app**, upload it via **Developer Portal**, and verify it works end-to-end with your Databricks Genie backend. 

---

## 5.1 Requirements (Teams & Tenant)

- A **Microsoft 365 tenant** where we can upload custom apps. We are using a Contoso Tenant (special) for this purpose 
- **Teams custom app upload** must be allowed. Head to **[Teams admin center](https://admin.teams.microsoft.com/)**:  
  `Teams apps → Setup policies → Add a policy → Upload custom apps = On` (we will attach our bot to this policy later)


![Genie](img/teams1.png)
  
- You can upload apps via **Teams client** (`Apps → Manage your apps → Upload an app → Upload a custom app`) or through **Developer Portal** (“Import app”, “Publish to org”). 


**We’ll need from previous sections**
- **Microsoft App ID** (Azure Bot’s App ID).
- **Messaging endpoint** (your Web App `/api/messages`).
- Optional: **Genie Space ID / endpoint** (already wired in the backend).

---


## 5.2 Create the Teams App Manifest

- For the next step we would now need to create a manifest file, there are multiple ways to create a manifest file, but for this example we will be using 
  Kyle Hale’s manifest, which can be found in his repo here --> https://github.com/kthejoker/genie-teams-bot.git
  Download the `genie-teams-app` folder from the repo, this template targets **Teams** and supports **personal, team, and group chat** scopes.

**Note**

- The folder also contains two files: color.png and outline.png. These are the bot logos and can be replaced with your custom logos. Ensure they retain the same names (color.png and outline.png), or else the changes will not be reflected


![Genie](img/teams2.png)


- Now in the editor of your choice clone the repo or open the downloaded `genie-teams-app` folder and navigate to the `manifest.json` file inside and replace the values in the keys **bots/botId** and **webApplicationInfo/id** with the Microsoft App ID from your Azure Bot resource


![Genie](img/teams3.png)


- After modyfying and save the `manifest.json` file we will need to create a new version of the manifest to upload it in Teams. So, open the terminal in your editor and navigate to the `genie-teams-app`folder and run the    following command (for windows users):

  ```
  Compress-Archive -Path * -DestinationPath genie-teams.zip
  
  ```

  A new zip file will be created. Keep this file as we need to upload it into Teams


![Genie](img/teams4.png)


## 5.3 Upload the Manifest file & Publish the App in Teams

In this step we will upload the 'manifest' folder we generated to Teams, at this time we will be doing this via the **Developer Portal**. For this we will need our Teams Account (Contoso) or one with proper permissions.

- Let's sign in into Microsoft Teams and in the left sidebar search for `Developer Portal` and click the option **Import an app**


  ![Genie](img/teams5.png)


- It will open an import menu wizard. Go ahead and upload the `zip` folder that we created previously containing the manifest file


  ![Genie](img/teams6.png)


- Your new app will be displayed in Teams but is not published yet

  ![Genie](img/teams7.png)
  

- Before distribute the app to the Org let's attach this app to the policy we created at the beginning. This is to enable the distribution of this App.
  Navigate to **[Teams admin center](https://admin.teams.microsoft.com/)** and go to `Teams apps → Setup policies → Search your new policy → Add apps (search your new app and add to the policy) → Save`


  ![Genie](img/teams8.png)


- Let's go back to the `Developer Portal` in the Teams client and search for our App again, click on `Distribute` and select `Publish to your organization`
  The App will require an approval from Admin. If so, you can go again as `Admin` to **[Teams admin center](https://admin.teams.microsoft.com/)** then search the app in the sidebar → `Teams Apps → Manage Apps → Search the    new App  and approve the request accordingly.


  ![Genie](img/teams9.png)


- The App will require an approval from Admin. If so, you can go again as `Admin` to **[Teams admin center](https://admin.teams.microsoft.com/)** then search the app in the sidebar → `Teams Apps → Manage Apps → Search the    new App and approve the request accordingly.


  ![Genie](img/teams10.png)
