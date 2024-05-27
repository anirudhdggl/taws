import boto3

client = boto3.client('iam')

iam_groups_raw = client.list_groups(MaxItems = 300)["Groups"]
iam_groups_name = []
iam_group_user_mapping = {}
iam_group_counter = 1
total_iam_groups = 0

print("Fetching IAM Groups...")

for iam_group in iam_groups_raw:
  iam_groups_name.append(iam_group["GroupName"])

total_iam_groups = len(iam_groups_name)

print(str(total_iam_groups) + " IAM groups fetched!")
print("IAM Group: IAM Users")

for iam_group in iam_groups_name:

  # Exclude automation groups
  if iam_group.startswith("AutomationGroup"):
    print("[" + str(iam_group_counter) + "/" + str(total_iam_groups) + "] Skipping automation group " + iam_group)
    iam_group_counter = iam_group_counter + 1
    continue

  # Fetch users in the group
  print("[" + str(iam_group_counter) + "/" + str(total_iam_groups) + "] Fetching users for " + iam_group + " group")
  iam_group_details = client.get_group(GroupName = iam_group)
  print("Found " + str(len(iam_group_details["Users"])) + " users in the group")

  # Add users to the map
  iam_group_user_mapping[iam_group] = []
  for iam_user in iam_group_details["Users"]:
    iam_group_user_mapping[iam_group].append(iam_user["UserName"])
  
  iam_group_counter = iam_group_counter + 1

print("IAM Group <> IAM User Mapping\n---------------------------")
print("Total IAM Groups: " + str(len(iam_groups_name)))
for iam_group in iam_group_user_mapping:
  print(iam_group + ": " + ",".join(iam_group_user_mapping[iam_group]))

print("---")
