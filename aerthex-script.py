@aerthexscript(
    name="Roblox User Info v1.3",
    author="thedorekaczynski",
    description="Fetches information about a Roblox user.",
    usage="<p>roblox <username> [--img]"
)
def RobloxScript():
    """
    ROBLOX USER INFO SCRIPT
    -----------------------
    
    This script allows users to search for Roblox user information using the Roblox API.
    
    COMMANDS:
    <p>roblox <username> [--img]      - Search for a user (add --img flag to show avatar)
    <p>robloxid <user_id> [--img]     - Search for a user by ID (add --img flag to show avatar)
    <p>rbtoggleimg                     - Toggle whether avatars are shown by default
    
    EXAMPLES:
    <p>roblox Builderman             - Shows info for user Builderman (no avatar)
    <p>roblox Builderman --img       - Shows info for Builderman with avatar
    <p>robloxid 156 --img            - Shows info for user with ID 156 with avatar
    
    NOTES:
    - By default, images are NOT shown to keep responses clean
    - You can permanently enable images with <p>rbtoggleimg
    - Or temporarily show an image for a specific search using --img
    
    API ENDPOINTS USED:
    - https://users.roblox.com/v1/usernames/users - For username lookup
    - https://users.roblox.com/v1/users/{user_id} - For basic user information
    - https://users.roblox.com/v1/users/{user_id}/status - For user status
    - https://thumbnails.roblox.com/v1/users/avatar - For user avatar images
    """
    import aiohttp
    import asyncio
    import json
    from datetime import datetime

    # Configuration keys
    IMAGE_CONFIG_KEY = "roblox_show_images"
    
    # Set default configurations if not already set
    try:
        if getConfigData().get(IMAGE_CONFIG_KEY) is None:
            updateConfigData(IMAGE_CONFIG_KEY, False)  # Default to NOT showing images
    except:
        print("Error accessing config, defaulting to not showing images", type_="WARNING")
    
    @bot.command(name="rbtoggleimg", description="Toggle whether Roblox user avatars are shown")
    async def toggle_roblox_images(ctx):
        """
        Toggles the default setting for displaying Roblox user avatars.
        This command is named specifically to avoid conflicts with other toggleimg commands.
        """
        await ctx.message.delete()
        
        try:
            current_setting = getConfigData().get(IMAGE_CONFIG_KEY, False)
            new_setting = not current_setting
            updateConfigData(IMAGE_CONFIG_KEY, new_setting)
            
            status = "enabled" if new_setting else "disabled"
            await ctx.send(f"Roblox user avatars are now **{status}**")
        except Exception as e:
            print(str(e), type_="ERROR")
            await ctx.send(f"Error toggling image setting: {str(e)}")

    async def get_user_id_by_username(session, username):
        """
        Get user ID from username using Roblox API
        
        Args:
            session: aiohttp ClientSession object
            username: The Roblox username to look up
            
        Returns:
            User ID as integer or None if not found
        """
        url = "https://users.roblox.com/v1/usernames/users"
        payload = {
            "usernames": [username],
            "excludeBannedUsers": False
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("data") and len(data["data"]) > 0:
                    return data["data"][0]["id"]
            return None

    async def get_user_info(session, user_id):
        """
        Get detailed user info using Roblox API
        
        Args:
            session: aiohttp ClientSession object
            user_id: The Roblox user ID to look up
            
        Returns:
            Dictionary containing user data or None if retrieval fails
        """
        url = f"https://users.roblox.com/v1/users/{user_id}"
        headers = {
            "Accept": "application/json"
        }
        
        user_data = {}
        
        # Get basic user info
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                user_data.update(data)
            else:
                print(f"Error fetching user info, status: {response.status}", type_="ERROR")
                return None
        
        # Get last online status and join date
        url = f"https://users.roblox.com/v1/users/{user_id}/status"
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                user_data["status"] = data.get("status", "")
            else:
                print(f"Error fetching status, continuing with partial data", type_="WARNING")
        
        return user_data

    async def get_avatar_url(session, user_id):
        """
        Get avatar thumbnail URL for a user
        
        Args:
            session: aiohttp ClientSession object
            user_id: The Roblox user ID to get avatar for
            
        Returns:
            URL to the avatar image or None if retrieval fails
        """
        url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=180x180&format=Png&isCircular=false"
        headers = {
            "Accept": "application/json"
        }
        
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("data") and len(data["data"]) > 0:
                    return data["data"][0].get("imageUrl")
            print(f"Error fetching avatar, status: {response.status}", type_="WARNING")
            return None

    @bot.command(name="roblox", usage="<username> [--img]", description="Fetches user info from Roblox")
    async def roblox_user(ctx, *, args: str):
        """
        Looks up a Roblox user by username and displays their information
        
        Args:
            args: String containing username and optional --img flag
        """
        await ctx.message.delete()
        
        # Check if --img flag is present
        show_image = False
        if args.endswith(" --img") or args == "--img":
            show_image = True
            username = args.replace(" --img", "").strip()
        elif args.startswith("--img "):
            show_image = True
            username = args.replace("--img ", "").strip()
        else:
            username = args.strip()
            # Check global setting if no override
            try:
                show_image = getConfigData().get(IMAGE_CONFIG_KEY, False)
            except:
                show_image = False  # Default if config fails
        
        print(f"Looking up Roblox user: '{username}'", type_="DEBUG")
        print(f"Show image setting: {show_image}", type_="DEBUG")
        
        msg = await ctx.send(f"Getting Roblox information for user '{username}', please wait...")
        
        # Save current private setting and update it
        current_private = getConfigData().get("private")
        updateConfigData("private", False)
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with aiohttp.ClientSession() as session:
                # First get user ID from username
                user_id = await get_user_id_by_username(session, username)
                
                if not user_id:
                    await forwardEmbedMethod(
                        channel_id=ctx.channel.id,
                        content=f"❌ **User '{username}' not found on Roblox.**",
                        title="Roblox User Info"
                    )
                    await msg.delete()
                    updateConfigData("private", current_private)
                    return
                
                # Get detailed user info
                user_data = await get_user_info(session, user_id)
                
                if not user_data:
                    await forwardEmbedMethod(
                        channel_id=ctx.channel.id,
                        content=f"❌ **Failed to fetch information for user '{username}'.**",
                        title="Roblox User Info"
                    )
                    await msg.delete()
                    updateConfigData("private", current_private)
                    return
                
                # Get avatar URL if needed
                avatar_url = None
                if show_image:
                    avatar_url = await get_avatar_url(session, user_id)
                
                # Format the creation date
                created_date = "Unknown"
                if "created" in user_data:
                    try:
                        date_str = user_data["created"].split("T")[0]
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                        created_date = date_obj.strftime("%d %B %Y")
                    except:
                        created_date = user_data.get("created", "Unknown")
                
                # Prepare user info content
                display_name = user_data.get("displayName", "None")
                profile_url = f"https://www.roblox.com/users/{user_id}/profile"
                description = user_data.get("description", "No description available.")
                if not description.strip():
                    description = "No description available."
                
                status = user_data.get("status", "")
                if not status.strip():
                    status = "None"
                
                content = f"""Username: **{user_data.get('name', username)}**
Display Name: **{display_name}**
User ID: **{user_id}**
Account Created: **{created_date}**
Status: **{status}**
Description: **{description}**
Profile URL: **[{user_data.get('name', username)}'s Profile]({profile_url})**"""

                # Send the embed with all info and the avatar image if requested
                await forwardEmbedMethod(
                    channel_id=ctx.channel.id,
                    content=content,
                    title="Roblox User Info",
                    image=avatar_url if show_image else None
                )
            
            # Restore original private setting
            updateConfigData("private", current_private)
            await msg.delete()
            
        except Exception as e:
            print(str(e), type_="ERROR")
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                content=f"❌ **Error occurred: {str(e)}**",
                title="Roblox User Info"
            )
            updateConfigData("private", current_private)
            await msg.delete()
    
    @bot.command(name="robloxid", usage="<user_id> [--img]", description="Fetches user info from Roblox by ID")
    async def roblox_user_by_id(ctx, *, args: str):
        """
        Looks up a Roblox user by their numeric ID and displays their information
        
        Args:
            args: String containing user ID and optional --img flag
        """
        await ctx.message.delete()
        
        # Check if --img flag is present
        show_image = False
        if args.endswith(" --img") or args == "--img":
            show_image = True
            user_id_str = args.replace(" --img", "").strip()
        elif args.startswith("--img "):
            show_image = True
            user_id_str = args.replace("--img ", "").strip()
        else:
            user_id_str = args.strip()
            # Check global setting if no override
            try:
                show_image = getConfigData().get(IMAGE_CONFIG_KEY, False)
            except:
                show_image = False  # Default if config fails
        
        # Validate that user_id is a number
        if not user_id_str.isdigit():
            await ctx.send("❌ User ID must be a number.")
            return
        
        user_id = int(user_id_str)
        print(f"Looking up Roblox user ID: '{user_id}'", type_="DEBUG")
        print(f"Show image setting: {show_image}", type_="DEBUG")
        
        msg = await ctx.send(f"Getting Roblox information for user ID '{user_id}', please wait...")
        
        # Save current private setting and update it
        current_private = getConfigData().get("private")
        updateConfigData("private", False)
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with aiohttp.ClientSession() as session:
                # Get detailed user info
                user_data = await get_user_info(session, user_id)
                
                if not user_data:
                    await forwardEmbedMethod(
                        channel_id=ctx.channel.id,
                        content=f"❌ **Failed to fetch information for user ID '{user_id}'.**",
                        title="Roblox User Info"
                    )
                    await msg.delete()
                    updateConfigData("private", current_private)
                    return
                
                # Get avatar URL if needed
                avatar_url = None
                if show_image:
                    avatar_url = await get_avatar_url(session, user_id)
                
                # Format the creation date
                created_date = "Unknown"
                if "created" in user_data:
                    try:
                        date_str = user_data["created"].split("T")[0]
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                        created_date = date_obj.strftime("%d %B %Y")
                    except:
                        created_date = user_data.get("created", "Unknown")
                
                # Prepare user info content
                username = user_data.get("name", f"User {user_id}")
                display_name = user_data.get("displayName", "None")
                profile_url = f"https://www.roblox.com/users/{user_id}/profile"
                description = user_data.get("description", "No description available.")
                if not description.strip():
                    description = "No description available."
                
                status = user_data.get("status", "")
                if not status.strip():
                    status = "None"
                
                content = f"""Username: **{username}**
Display Name: **{display_name}**
User ID: **{user_id}**
Account Created: **{created_date}**
Status: **{status}**
Description: **{description}**
Profile URL: **[{username}'s Profile]({profile_url})**"""

                # Send the embed with all info and the avatar image if requested
                await forwardEmbedMethod(
                    channel_id=ctx.channel.id,
                    content=content,
                    title="Roblox User Info",
                    image=avatar_url if show_image else None
                )
            
            # Restore original private setting
            updateConfigData("private", current_private)
            await msg.delete()
            
        except Exception as e:
            print(str(e), type_="ERROR")
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                content=f"❌ **Error occurred: {str(e)}**",
                title="Roblox User Info"
            )
            updateConfigData("private", current_private)
            await msg.delete()

RobloxScript()