import subprocess

def get_wifi_passwords():
    profiles_data = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles'],
        shell=True, text=True
    )
    
    profiles = [line.split(":")[1].strip() for line in profiles_data.split("\n") if "All User Profile" in line]
    
    wifi_list = []
    
    for profile in profiles:
        profile_info = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
            shell=True, text=True
        )
        
        password_lines = [line.split(":")[1].strip() for line in profile_info.split("\n") if "Key Content" in line]
        password = password_lines[0] if password_lines else "N/A"
        
        wifi_list.append((profile, password))
    
    
    print("\nSaved Wi-Fi Networks & Passwords:\n")
    for wifi in wifi_list:
        print(f"📶 {wifi[0]} — 🔑 {wifi[1]}")

get_wifi_passwords()
