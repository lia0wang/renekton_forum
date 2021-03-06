# Overview
- The **Renekton Forum** is an online discussion board for **League of Legends** where players can ask questions, share their experiences, and discuss topics of mutual interest.

## Admin
- The admin user owns all rights include add, edit, delete and can give authorization to all the topics, posts and users.

## User
- A user can add a topic and becomes the owner of the topic.
- A user can access any topic in the forum.
- A user can add posts in others' topics where he/she is even not an owner of the topic.
- A user cannot edit others' posts and can only edit his/her own post.

## Topic and Post
- Topic and Post are displayed by time order.
- Topic and Post both have the owner attribute.
- Topic and Post both associate with each user through **ForeignKey User**.

## Logs
- 27/11/2021 -> make the **edit post button** invisible if the user is not the owner of the post.
- 28/11/2021 -> fix the issue that the created date of post was not shown on the page hosted by heroku server but working properly on my local machine.