# import requests
# import json
# from json import JSONDecodeError


# # Specify the export format as PASCAL VOC
# export_format = "pascal_voc"


# # Use the Roboflow API to export the dataset
# url = f"https://universe.roboflow.com/ds/0D5GLOhobO?key=N8mG1WSf3w"
# response = requests.get(url)
# if response.status_code != 200:
#     print(f"Error: {response.text}")
# else:
#     try:
#         export_url = json.loads(response.text)["url"]
#     except JSONDecodeError as e:
#         print(f"Error occured: {e}")

# # Download the exported dataset using the export URL
# response = requests.get(export_url)
# with open("C:/Users/ilaya/LaunchVideos/VideoAfter/", "wb") as f:
#     f.write(response.content)

# print("Dataset exported successfully.")