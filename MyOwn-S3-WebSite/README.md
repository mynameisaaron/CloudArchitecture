# My Own Static S3 Website
![](ReadMe_Files/gittile.jpg)
\
[Located here](https://www.aaronbrightman.com)


This is a little tutorial to create a static website hosted on the AWS Cloud.  Maybe you have a website of your own, or several.



Using an S3 bucket to host a website is not re-inventing the wheel.  Besides the having your files operate with native compatibility of the many AWS services, I want to highlight few benefits over more popular hosting solutions:

1) **Cost vs Performance** - I am only paying for the S3 storage that I am using, it’s a few cents a month and in conjunction with CloudFront (AWS's CDN service) my website is Cached Globally and can be downloaded at any of the 600 'Points-of-Presence' edge locations.  Wherever you are located, from Detroit to Manilla, to Buenos Aires, note how fast this website loads!

2) **Durability & Availability** - [According to](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html) corporate literature and services agreements.  You get the “eleven-nines” of data durability: 99.999999999% of your 'objects' (i.e. Files) are guaranteed to persist without corruption: If you had 10 million files hosted, you can expect to lose a file every 10,000 years, while your availability is guaranteed 99.99%, or 53 minutes downtime a year.

4) **Granular Security** - S3 Resource policies allow you to granulate the permissions of your entire S3 bucket, entire folders, or each individual file.  Once you get the hang of how resource policies work, they are very straightforward and default to a very secure white-list model where your resources are created with no permissions (or no access).  You have to manually configure to expose your resources in order for users or services like CloudFront to use them.

This is not an extensive list, I could go on, let's get into it!

## Get your Files into an S3 Bucket

