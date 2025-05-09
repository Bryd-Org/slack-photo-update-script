# Slack-photo-update-script

## Installing a Slack App and configuring token

### **Prerequisites**
- Your workspace is part of the Enterprise Grid.
- You need admin privileges in your Slack workspace to perform the steps.
- Docker is installed on your machine and is able lo launch linux containers.

### **Step 1: Create a Slack App**
1. Go to the [Slack API Dashboard](https://api.slack.com/apps) and click **Create an App**.
2. Choose **From manifest**.
3. Select a workspace in your Enterprise Grid.
4. Copy-paste app manifest from `slack_app_manifest.json` file.
5. Click **Create**.

### **Step 2: Install the App with Org-Wide Opt-In**
1. In the **Settings** section, scroll to the **Install App** section.
2. Click **Install to Organization**.
3. Authorize the app with the required permissions.

### **Step 3: Acquire the Admin Token**
1. Navigate to the **OAuth & Permissions** section of your app.
2. After installation, copy the **User OAuth Token**.

### **Step 4: Set Token into this App**
1. Create `.secrets.toml` in this repository.
2. Insert these lines into secrets file, replacing `YOUR_TOKEN` with valid slack **User OAuth Token**.
   ```toml
   [default]
   SLACK_USER_TOKEN = "YOUR_TOKEN"
   ```

### **Common Issues**
- **Invalid Token**: Confirm you’re using the correct token from the **OAuth & Permissions** section.
- **Org-Wide Opt-In Failure**: Verify that the app is installed at the organization level and not just a single workspace.

---
---

### **Script container testing** (*test*)

All the scripts here are run as linux docker containers. To verify that you operating system is able to run 
them you might use this test command. No additional preparation required.

   
1. **Run process**  
   - Execute the following command to assign admin or owner role:
     ```bash
     docker-compose up test
     ```

**Result:**

After container assembly it should log that script is starting, then working and sleeping 5 seconds and then 
correct exit with code 0.

Correct testing log ends with these lines:
```log
test-1  | [2025-01-21 09:40:00,676][INFO] main.py:87 | Script self test is working. Sleeping 5 seconds
test-1  | [2025-01-21 09:40:05,679][INFO] main.py:89 | Script self test finished
test-1 exited with code 0

```
---

### **Update user photos** (*update-user-photos*)

This script updates the profile photos of users based on the provided instructions.

1. **Prepare the instructions file**  
   - Open the `instructions/update_photos.csv` file.  
   - Populate it with `user_email` and `photo_url` (should be a valid JPG file) values.
   - Each line represents a single user and their new photo URL.
   
2. **Run process**  
   - Execute the following command to update user profile photos:
     ```bash
     docker-compose up update-user-photos
     ```

**Result:**  

After execution, the profile photos of users specified in the `update_photos.csv` file will be updated with the provided photo URLs.

---
