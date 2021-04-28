# Pitches 

## WebApp

<table>
<tr>
<td>
  A web App that helps users introduce themselve with short pitches.
</td>
</tr>
</table>


## Development server

Create start.sh file in the root directory.
Add the following command to your start.sh file.
- export NEWS_API_KEY=<'GET KEY FROM NEWSAPI'>
- export MAIL_USERNAME=<'YOUR EMAIL ADDRESS>
- export MAIL_PASSWORD=<'YOUR EMAIL PASSWORD'>

- python3 manage.py server

Run `.\start.sh` for a dev server. Navigate to `http://localhost:5000/`. The app will automatically reload if you change any of the source files.

## [Usage](https://pitcheshotline.herokuapp.com/)

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/benjaminbills/pitches/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/benjaminbills/pitches/issues/new). Please include sample queries and their corresponding results.

## Built with

- [Python](https://www.python.org/)- version 3.8.5.
- [Bootstrap](https://getbootstrap.com/)- version 5.0
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - version 1.1.2
- [Google Fonts](https://fonts.google.com/)
- [Check requirements for more details](https://github.com/benjaminbills/pitches/blob/master/requirements.txt)

## To-do

- Modify UX/UI for better experience.

## [License](https://github.com/benjaminbills/pitches/blob/master/License)

MIT © [Benjamin Obafemi ](https://github.com/benjaminbills)
