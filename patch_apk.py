import sys
import shutil
import os
import socket

def add_network_security_config(path_to_app: str) -> None:
    path_to_xml = path_to_app + '/res/xml'
    shutil.copyfile('./network_security_config.xml', path_to_xml + '/network_security_config.xml')

def patch_android_manifest(path_to_app: str) -> None:
    path_to_manifest = path_to_app + '/AndroidManifest.xml'
    with open(path_to_manifest, 'r') as f:
        manifest = f.read()
    
    strings_to_patch = '<application'
    if 'android:allowBackup="true"' not in manifest:
        strings_to_patch += ' android:allowBackup="true"'
    if 'android:networkSecurityConfig="@xml/network_security_config"' not in manifest:
        strings_to_patch += ' android:networkSecurityConfig="@xml/network_security_config"'
    manifest = manifest.replace('<application', strings_to_patch)
    with open(path_to_manifest, 'w') as f:
        f.write(manifest)
    f.close()

def get_ip_address() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


def patch_flutter_app(path_to_apk: str) -> None:
    print('Choose option 1, and this is you IP address: ' + get_ip_address())
    shutil.copyfile(path_to_apk, './app.apk')
    os.system('reflutter app.apk')
    os.system('java -jar uber-apk-signer-1.3.0.jar --apk release.RE.apk')
    os.system('adb install release.RE-aligned-debugSigned.apk')
    os.remove('./app.apk')
    os.remove('./release.RE.apk')
    os.remove('./release.RE-aligned-debugSigned.apk')
    os.remove('./release.RE-aligned-debugSigned.apk.idsig')
    shutil.rmtree('./release')


def patch_app(path_to_apk: str) -> None:
    shutil.copyfile(path_to_apk, './app.apk')
    os.system('echo "g" | apktool d app.apk')
    add_network_security_config('./app')
    patch_android_manifest('./app')  
    os.system('echo "g" | apktool b app')
    os.system('java -jar uber-apk-signer-1.3.0.jar --apk app\\dist\\app.apk')
    os.system('adb install app\\dist\\app-aligned-debugSigned.apk')
    os.remove('./app.apk')
    shutil.rmtree('./app')
    shutil.rmtree('./release')



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python patch_apk.py <path_to_apk> <patch_type - 0: java, 1: flutter>')
        print('Example: python patch_apk.py ./app.apk 0')
        sys.exit(1)
    path_to_apk = sys.argv[1]
    patch_type = sys.argv[2]
    if patch_type == '0':
        patch_app(path_to_apk)
    elif patch_type == '1':
        patch_flutter_app(path_to_apk)
    else:
        print('Invalid patch type')
        sys.exit(1)
