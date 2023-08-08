import requests
import sys
import os

s = requests.session()
s.headers.update({
    "Authorization": f"Bot {os.environ['DISCORD_BOT_TOKEN']}"
})


def get_role_by_name(guild_id, name):
    r = s.get(f"https://discord.com/api/guilds/{guild_id}/roles")
    return list(filter(lambda r: r["name"] == name, r.json()))[0]["id"]


def add_role_to_user(guild_id, user_id, role_id):
    s.put(f"https://discord.com/api/guilds/{guild_id}/members/{user_id}/roles/{role_id}").raise_for_status()


def remove_role_from_user(guild_id, user_id, role_id):
    s.delete(f"https://discord.com/api/guilds/{guild_id}/members/{user_id}/roles/{role_id}").raise_for_status()


if __name__ == "__main__":
    ***REMOVED***= "***REMOVED***"

    part_time_users = [
        "***REMOVED***",
        "***REMOVED***"
    ]

    league = get_role_by_name(***REMOVED***, "League")

    if sys.argv[1] == "add":
        for user in part_time_users:
            add_role_to_user(***REMOVED***, user, league)
    elif sys.argv[1] == "remove":
        for user in part_time_users:
            remove_role_from_user(***REMOVED***, user, league)
    else:
        print("I don't know what that is.")
