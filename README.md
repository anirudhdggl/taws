# TAWS

TAWS or **T**ools for **AWS** is a collection of various codes and tools, that I wish I had when I needed them the most.

## Tools and codes we have

- [Force download files from s3 bucket using lambda function] (#https://github.com/anirudhdggl/taws/#forceD)

## forceD

forceD or forceDownload is the script that I had to figure out the hard way. When I was unable to find a working solution anywhere on the internet, I decided to write it on my own.

Most of the solutions for applying forced download of files from s3 out there, involves creating a pre-signed URL and setting **content-disposition** header to *attachment*.

But in my case I needed to set the header irrespective of the mode of download.

### How to use

1. Activate events in the required s3 bucket(s) for lambda function [learn how](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-event-notifications.html "AWS docs").
2. Select all write operations for notification trigger.
3. Assign proper permissions to enable lambda function to read and write from and to s3 buckets.
4. Copy and paste the forceD.py to your lambda function.
5. Customize the script as per your needs.
6. Save the function using *Save* Button.
7. Test the function using *Test* button. If you find any compile time errors, make changes and go to step 6
8. Upload any file to any folder in bucket and see the changes.

**Note**: Any compile time issue found in the lambda function can only be because of any modifications made by you. I've taken utmost care to make sure that the script is error-free. If you still find any errors do let me know

### How does the script work

**Variables Used**
|variable name           | Use |
|:----------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bucket                 | It used to store the bucket name that triggered the function                                                                                                    |
| key                    | It stores the name of the object that was uploaded                                                                                                              |
| objectUploadedInFolder | This tells the script whether the object is stored in a folder within the bucket or uploaded simply to the bucket. [see here](#improvements-forceD)             |
| source                 | The location of the file uploaded                                                                                                                               |
| destination            | Location of file in uploads folder where new file will be created                                                                                               |
| path                   | Use this variable as destination if you do not want your new file name to have a plus sign instead of spaces,e.g., "hello there.txt" instead of hello+there.txt |

**Methodology**
Whenever any file is uploaded to any folder in the bucket, the lambda function is triggered. This function will then copy the object uploaded, the object that triggered it, and while copying will set it's content-disposition value to attachment.

**Improvements to be made**
[] The script is unable to do the copy task for files that are not uploaded to any folder and rather directly to s3 base directory.

<p>&nbsp;</p>

>For any improvements and suggestions feel free to open an issue, pull request or contact me.