import aiohttp
import aiofiles
import asyncio

# Define an asynchronous function to download an image from a given URL
async def download_image(url, filename):
    # Create an asynchronous session using aiohttp
    async with aiohttp.ClientSession() as session:
        # Make an asynchronous GET request to the URL
        async with session.get(url) as response:
            # Check if the request was successful (status code 200)
            if response.status == 200:
                # Open a file in write-binary mode using aiofiles
                f = await aiofiles.open(filename, mode='wb')
                # Write the response content to the file
                await f.write(await response.read())
                # Close the file
                await f.close()
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {filename}")

# Define an asynchronous function named function1
async def function1():
    print("func 1")
    # URL of the image to download
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    # Call the download_image function with the URL and a filename
    await download_image(URL, "instagram1.jpg")
    # Return a string
    return "Harry"

# Define an asynchronous function named function2
async def function2():
    print("func 2")
    # URL of the image to download
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    # Call the download_image function with the URL and a filename
    await download_image(URL, "instagram2.jpg")

# Define an asynchronous function named function3
async def function3():
    print("func 3")
    # URL of the image to download
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    # Call the download_image function with the URL and a filename
    await download_image(URL, "instagram3.jpg")

# Define the main asynchronous function to orchestrate the other functions
async def main():
    # Use asyncio.gather to run the three functions concurrently
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    # Print the list of results from the functions
    print(L)

# Run the main function using asyncio.run
asyncio.run(main())
