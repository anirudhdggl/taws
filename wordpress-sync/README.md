# Wordpress Sync

:warning: **warning**

These scripts are formed by commands that I have run seperately and one by one. Although they must work fine, but still I would recommend to test them somehow on a POC environment before running on your production environment.

## Components

This entire script is to be run in 4 parts,

1. db-sync script on the old installation
2. db-sync script on the new installation
3. efs-sync script on the old installation
4. efs-sync script on the new installation

## How does it work

Beginning with the **first step**, when you run db-sync.sh on old installation, it first of all installs aws cli and configures it. After that it takes a mysqldump of your entire database.

The script in itself creates a new bucket, adding a random 32-bit string to it's end to make it DNS compliable and unique. Once created, we upload the dump to that bucket.

Coming to the new destination, the script will then install the dump from the s3 bucket and import it into the new database.

You can additionally run wp search-replace, but for that you'll need to have wp-cli installed.

Similarly we upload everything from the source EFS to the destination EFS via a s3 bucket.

:information_source: You can also use DataSync for synchronizing EFS.

And I'll prefer you to use that, because it's AWS managed and less prone to errors, that unintentionally may be caused via scripts.

> If you feel any modifications or improvements could be made, do let me know. Or even better, open a PR.