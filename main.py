import json


def main():
    f = open("settings/setting.json")
    s = f.read()
    d = json.loads(s)
    f.close()

    subcommand = "title"
    subdict = d["title_type"][subcommand]
    print(f'/title {d["entity"]} {subcommand} {{"{subdict["type"]}":"{subdict["value"]}"}}')


if __name__ == '__main__':
    main()
