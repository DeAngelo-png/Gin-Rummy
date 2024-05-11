#      ___       ___       ___       ___       ___       ___   
#     /\  \     /\  \     /\  \     /\  \     /\  \     /\__\  
#    /::\  \   /::\  \   /::\  \   /::\  \   /::\  \   /:/ _/_ 
#   /::\:\__\ /::\:\__\ /::\:\__\ /::\:\__\ /:/\:\__\ /::-"\__\
#   \;:::/  / \:\:\/  / \/\::/  / \/\::/  / \:\ \/__/ \;:;-",-"
#    |:\/__/   \:\/  /     \/__/    /:/  /   \:\__\    |:|  |  
#     \|__|     \/__/               \/__/     \/__/     \|__|  
#           ___       ___       ___       ___       ___        
#          /\  \     /\__\     /\__\     /\__\     /\__\       
#         /::\  \   /:/ _/_   /::L_L_   /::L_L_   |::L__L      
#        /::\:\__\ /:/_/\__\ /:/L:\__\ /:/L:\__\  |:::\__\     
#        \;:::/  / \:\/:/  / \/_/:/  / \/_/:/  /  /:;;/__/     
#         |:\/__/   \::/  /    /:/  /    /:/  /   \/__/        
#          \|__|     \/__/     \/__/     \/__/                 
#
#   I am not responsible for any trouble you get with your ISP
#  or any viruses you obtain, by using this tool you agree that
#     this is for educational purposes only. (Use a vpn lol)
import webbrowser, time, sys, os

# Constants
wt = 1 # Wait time before each tab opens

# Repack search aggregation (fancy way of saying searching all the listed sites)
def open_tabs_with_search_query(search_query, file_name): # reads from the file and opens the websites with the search query
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "websites.txt")
    with open(file_path, 'r') as file:
        websites = file.readlines()
        for website in websites:
            website = website.strip() # remove newline characters
            webbrowser.open_new_tab(website + search_query)
            time.sleep(wt)

def main():
    sys.stdout.write("\x1b]2; [♠] Repack Rummy \x07")
    print("""
    [38;2;255;0;0m [0m[38;2;252;3;3m [0m[38;2;249;6;6m_[0m[38;2;246;9;9m_[0m[38;2;243;12;12m_[0m[38;2;240;15;15m [0m[38;2;237;18;18m [0m[38;2;234;21;21m [0m[38;2;231;24;24m [0m[38;2;228;27;27m [0m[38;2;225;30;30m [0m[38;2;222;33;33m [0m[38;2;219;36;36m [0m[38;2;216;39;39m [0m[38;2;213;42;42m [0m[38;2;210;45;45m [0m[38;2;207;48;48m [0m[38;2;204;51;51m [0m[38;2;201;54;54m [0m[38;2;198;57;57m [0m[38;2;195;60;60m [0m[38;2;192;63;63m [0m[38;2;189;66;66m [0m[38;2;186;69;69m [0m[38;2;183;72;72m_[0m[38;2;180;75;75m [0m[38;2;177;78;78m [0m[38;2;174;81;81m [0m[38;2;171;84;84m [0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m [0m[38;2;159;96;96m [0m[38;2;156;99;99m [0m[38;2;153;102;102m [0m[38;2;150;105;105m [0m[38;2;147;108;108m [0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m|[0m[38;2;249;6;6m [0m[38;2;246;9;9m_[0m[38;2;243;12;12m [0m[38;2;240;15;15m\[0m[38;2;237;18;18m_[0m[38;2;234;21;21m_[0m[38;2;231;24;24m_[0m[38;2;228;27;27m [0m[38;2;225;30;30m_[0m[38;2;222;33;33m [0m[38;2;219;36;36m_[0m[38;2;216;39;39m_[0m[38;2;213;42;42m [0m[38;2;210;45;45m [0m[38;2;207;48;48m_[0m[38;2;204;51;51m_[0m[38;2;201;54;54m [0m[38;2;198;57;57m_[0m[38;2;195;60;60m [0m[38;2;192;63;63m_[0m[38;2;189;66;66m_[0m[38;2;186;69;69m|[0m[38;2;183;72;72m [0m[38;2;180;75;75m|[0m[38;2;177;78;78m_[0m[38;2;174;81;81m_[0m[38;2;171;84;84m [0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m [0m[38;2;159;96;96m [0m[38;2;156;99;99m [0m[38;2;153;102;102m [0m[38;2;150;105;105m [0m[38;2;147;108;108m [0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m|[0m[38;2;249;6;6m [0m[38;2;246;9;9m [0m[38;2;243;12;12m [0m[38;2;240;15;15m/[0m[38;2;237;18;18m [0m[38;2;234;21;21m-[0m[38;2;231;24;24m_[0m[38;2;228;27;27m)[0m[38;2;225;30;30m [0m[38;2;222;33;33m'[0m[38;2;219;36;36m_[0m[38;2;216;39;39m [0m[38;2;213;42;42m\[0m[38;2;210;45;45m/[0m[38;2;207;48;48m [0m[38;2;204;51;51m_[0m[38;2;201;54;54m`[0m[38;2;198;57;57m [0m[38;2;195;60;60m/[0m[38;2;192;63;63m [0m[38;2;189;66;66m_[0m[38;2;186;69;69m|[0m[38;2;183;72;72m [0m[38;2;180;75;75m/[0m[38;2;177;78;78m [0m[38;2;174;81;81m/[0m[38;2;171;84;84m [0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m [0m[38;2;159;96;96m [0m[38;2;156;99;99m [0m[38;2;153;102;102m [0m[38;2;150;105;105m [0m[38;2;147;108;108m [0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m|[0m[38;2;249;6;6m_[0m[38;2;246;9;9m|[0m[38;2;243;12;12m_[0m[38;2;240;15;15m\[0m[38;2;237;18;18m_[0m[38;2;234;21;21m_[0m[38;2;231;24;24m_[0m[38;2;228;27;27m|[0m[38;2;225;30;30m [0m[38;2;222;33;33m.[0m[38;2;219;36;36m_[0m[38;2;216;39;39m_[0m[38;2;213;42;42m/[0m[38;2;210;45;45m\[0m[38;2;207;48;48m_[0m[38;2;204;51;51m_[0m[38;2;201;54;54m,[0m[38;2;198;57;57m_[0m[38;2;195;60;60m\[0m[38;2;192;63;63m_[0m[38;2;189;66;66m_[0m[38;2;186;69;69m|[0m[38;2;183;72;72m_[0m[38;2;180;75;75m\[0m[38;2;177;78;78m_[0m[38;2;174;81;81m\[0m[38;2;171;84;84m [0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m [0m[38;2;159;96;96m [0m[38;2;156;99;99m [0m[38;2;153;102;102m [0m[38;2;150;105;105m [0m[38;2;147;108;108m [0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m [0m[38;2;249;6;6m [0m[38;2;246;9;9m [0m[38;2;243;12;12m [0m[38;2;240;15;15m [0m[38;2;237;18;18m [0m[38;2;234;21;21m [0m[38;2;231;24;24m [0m[38;2;228;27;27m|[0m[38;2;225;30;30m_[0m[38;2;222;33;33m|[0m[38;2;219;36;36m [0m[38;2;216;39;39m_[0m[38;2;213;42;42m [0m[38;2;210;45;45m\[0m[38;2;207;48;48m_[0m[38;2;204;51;51m [0m[38;2;201;54;54m [0m[38;2;198;57;57m_[0m[38;2;195;60;60m [0m[38;2;192;63;63m_[0m[38;2;189;66;66m [0m[38;2;186;69;69m_[0m[38;2;183;72;72m_[0m[38;2;180;75;75m [0m[38;2;177;78;78m [0m[38;2;174;81;81m_[0m[38;2;171;84;84m [0m[38;2;168;87;87m_[0m[38;2;165;90;90m_[0m[38;2;162;93;93m [0m[38;2;159;96;96m_[0m[38;2;156;99;99m [0m[38;2;153;102;102m [0m[38;2;150;105;105m_[0m[38;2;147;108;108m [0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m [0m[38;2;249;6;6m [0m[38;2;246;9;9m [0m[38;2;243;12;12m [0m[38;2;240;15;15m [0m[38;2;237;18;18m [0m[38;2;234;21;21m [0m[38;2;231;24;24m [0m[38;2;228;27;27m [0m[38;2;225;30;30m [0m[38;2;222;33;33m|[0m[38;2;219;36;36m [0m[38;2;216;39;39m [0m[38;2;213;42;42m [0m[38;2;210;45;45m/[0m[38;2;207;48;48m [0m[38;2;204;51;51m|[0m[38;2;201;54;54m|[0m[38;2;198;57;57m [0m[38;2;195;60;60m|[0m[38;2;192;63;63m [0m[38;2;189;66;66m'[0m[38;2;186;69;69m [0m[38;2;183;72;72m [0m[38;2;180;75;75m\[0m[38;2;177;78;78m|[0m[38;2;174;81;81m [0m[38;2;171;84;84m'[0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m\[0m[38;2;159;96;96m [0m[38;2;156;99;99m|[0m[38;2;153;102;102m|[0m[38;2;150;105;105m [0m[38;2;147;108;108m|[0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m [0m[38;2;249;6;6m [0m[38;2;246;9;9m [0m[38;2;243;12;12m [0m[38;2;240;15;15m [0m[38;2;237;18;18m [0m[38;2;234;21;21m [0m[38;2;231;24;24m [0m[38;2;228;27;27m [0m[38;2;225;30;30m [0m[38;2;222;33;33m|[0m[38;2;219;36;36m_[0m[38;2;216;39;39m|[0m[38;2;213;42;42m_[0m[38;2;210;45;45m\[0m[38;2;207;48;48m\[0m[38;2;204;51;51m_[0m[38;2;201;54;54m,[0m[38;2;198;57;57m_[0m[38;2;195;60;60m|[0m[38;2;192;63;63m_[0m[38;2;189;66;66m|[0m[38;2;186;69;69m_[0m[38;2;183;72;72m|[0m[38;2;180;75;75m_[0m[38;2;177;78;78m|[0m[38;2;174;81;81m_[0m[38;2;171;84;84m|[0m[38;2;168;87;87m_[0m[38;2;165;90;90m|[0m[38;2;162;93;93m_[0m[38;2;159;96;96m\[0m[38;2;156;99;99m_[0m[38;2;153;102;102m,[0m[38;2;150;105;105m [0m[38;2;147;108;108m|[0m[38;2;144;111;111m
    [0m[38;2;255;0;0m [0m[38;2;252;3;3m [0m[38;2;249;6;6m [0m[38;2;246;9;9m [0m[38;2;243;12;12m [0m[38;2;240;15;15m [0m[38;2;237;18;18m [0m[38;2;234;21;21m [0m[38;2;231;24;24m [0m[38;2;228;27;27m [0m[38;2;225;30;30m [0m[38;2;222;33;33m [0m[38;2;219;36;36m [0m[38;2;216;39;39m [0m[38;2;213;42;42m [0m[38;2;210;45;45m [0m[38;2;207;48;48m [0m[38;2;204;51;51m [0m[38;2;201;54;54m [0m[38;2;198;57;57m [0m[38;2;195;60;60m [0m[38;2;192;63;63m [0m[38;2;189;66;66m [0m[38;2;186;69;69m [0m[38;2;183;72;72m [0m[38;2;180;75;75m [0m[38;2;177;78;78m [0m[38;2;174;81;81m [0m[38;2;171;84;84m [0m[38;2;168;87;87m [0m[38;2;165;90;90m [0m[38;2;162;93;93m [0m[38;2;159;96;96m|[0m[38;2;156;99;99m_[0m[38;2;153;102;102m_[0m[38;2;150;105;105m/[0m[38;2;147;108;108m [0m[0m""")
    search_query = input("  [40;38;2;255;0;0m[[0m♠[40;38;2;243;12;12m][0m[40;38;2;231;24;24m [0m[40;38;2;219;36;36mS[0m[40;38;2;207;48;48me[0m[40;38;2;195;60;60ma[0m[40;38;2;183;72;72mr[0m[40;38;2;171;84;84mc[0m[40;38;2;159;96;96mh[0m[40;38;2;147;108;108m [0m➧ ")

if __name__ == "__main__":
    main()