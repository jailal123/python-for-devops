# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1


###### details of "f"#########################

    Yes, you're correct. Thank you for elaborating on the concept of f-strings.

To add more detail, f-strings provide a convenient and readable way to create strings with embedded expressions or variables. 
By prefixing a string with f or F, Python understands that it's an f-string, allowing you to directly embed Python expressions 
or variables within curly braces {} within the string.

For example:

python
Copy code
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
In this example, {name} and {age} are placeholders within the string that are replaced with the values of the variables name and 
age respectively when the string is formatted. This makes it easy to construct strings dynamically based on variable values.

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")



