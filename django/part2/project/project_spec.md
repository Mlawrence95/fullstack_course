# Project

1. Set up an app having the following model:

- User
  - first_name
  - last_name
  - email

2. Create a script to populate the database with fake info, performing necessary migrations.
Confirm that the data was populated correctly via the admin panel.

3. Create a view at `/users`. This should be a list of names + emails. Generate
the table using the typical template tag approach from the User model. The page
should look like:

```HTML
1. User Info
  - First Name: Bob
  - Last Name: Jenkins
  - Email: bob@jenkins.com

2. User Info
  - First Name: Allen
  - Last Name: Smith
  - Email: sdgf@gmail.com
```
4. Make sure there's a home page that forwards users to `/users`.
