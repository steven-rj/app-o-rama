def organize_apps():

    apps = sorted([("Big Clipboard", "clipb.main()"),
            ("YouTube Downloader", "yt.main()"),
            ("PDF-to-Speech", "pdf.main()")])


    sorted_apps_list = [[0, ("Exit Program", "sys.exit()")]]
    for num, app in enumerate(apps, 1):
        app_info = [num, app]
        sorted_apps_list.append(app_info) 

    return (sorted_apps_list)

if __name__ == "__main__":
    organize_apps()