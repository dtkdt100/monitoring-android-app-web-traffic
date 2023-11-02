# Monitoring Android App Web Traffic
View and edit your android app web traffic without a need to root your device.

#### Requirements:

 - [Burp suite](https://portswigger.net/burp/communitydownload)
 - [Apktool](https://apktool.org/docs/install)
 - Java
 - [uber apk signer](https://github.com/patrickfav/uber-apk-signer) - In repo
 - For flutter apps: [reflutter](https://github.com/ptswarm/reFlutter) - In repo
 - ADB (Optinal)

Note: With rooted phone you can use this tutorial -> https://blog.ropnop.com/configuring-burp-suite-with-android-nougat. The code in this repo will automate the steps in this article.

## Step 1 - Install burp cretificate

#### Configure the Burp Proxy listener
Follow steps 1 and 2 in the official burp website -> https://portswigger.net/burp/documentation/desktop/mobile/config-android-device

#### Donwload burp cretificate
In you android phone:
1. Open https://burp with your browser
2. Clink on "CA Certificate", the download will start
3. On your device settings go to: Security and privacy -> Encryption and credentials -> Install a cretificate -> CA Certificate. If you can't find it just search for: "Certificate"
5. Choose the downloaded cretficate

<details>
  <summary>Recorded Screen</summary>
  https://github.com/dtkdt100/monitoring-android-app-web-traffic/assets/63166757/a905460b-5861-45ef-a7b3-1ceb364deaac
</details>

## Step 2 - Patch APK

Run the follwing command: `python patch_apk.py <path_to_apk> <patch_type - 0: java, 1: flutter>`
Example:  `python patch_apk.py oneto50.apk 1`

Note: make sure the device is connected in debugger mode 
