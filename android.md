Android SDK setup from CLI:

1. Download command line tools under "## Command line tools only" on this page: https://developer.android.com/studio
2. Extract to C:\Android\sdk
3. As per https://stackoverflow.com/questions/65262340/cmdline-tools-could-not-determine-sdk-root, Rename the unpacked directory from **cmdline-tools** to **tools**, and place it under $C:/Android/cmdline-tools. Now it will look like $C:/Android/cmdline-tools/tools
4. Set ANDROID_SDK_ROOT environment variable
5. Set JAVA_HOME environment variable (KEYLANGAN SYA IG RUN FROM ADB USB DEBUG MODE)
6. Update %PATH% with  ![[Pasted image 20211010160947.png]]
7. `sdkmanager --list`
8. `sdkmanager "platform-tools"`
9. `sdkmanager "platforms;android-29"`
10. `sdkmanager --list | grep system-images`
11. Download image: `sdkmanager --install "system-images;android-29;google_apis_playstore;x86_64"`
12. Download and install HAXM: https://github.com/intel/haxm
13. Disable Hyper-V. See https://docs.microsoft.com/en-us/troubleshoot/windows-client/application-management/virtualization-apps-not-work-with-hyper-v
14. Create a new AVD. See https://developer.android.com/studio/command-line/avdmanager
	- System image: "system-images;android-29;google_apis_playstore;x86_64"
	- Command: `avdmanager create avd -n Android29 -k "system-images;android-29;google_apis_playstore;x86_64"`
15. `emulator -avd Android29 [-gpu host] [-no-snapshot-load]` to run
	1. no-spapshot-load = cold boot
16. To list all devices, run `adb devices`

ERROR: cannot add library vulkan-1.dll: failed
FIX: [flutter - Android Studio Emulator: cannot add library vulkan-1.dll: failed - Stack Overflow](https://stackoverflow.com/questions/65696048/android-studio-emulator-cannot-add-library-vulkan-1-dll-failed) JUST DOWNLOAD IT


## Reference
[1] https://medium.com/@vsburnett/how-to-set-up-an-android-emulator-in-windows-10-e0a3284b5f94
[2] CLI Tools: https://developer.android.com/studio/command-line
