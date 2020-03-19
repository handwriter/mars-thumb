from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE html>
               <html lang="en">
               <head>
                 <meta charset="utf-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1">
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
               </head>
               <body>
               <h2 align="center" style="color:Black">Пейзажи Марса</h2>
               <div class="container">
                 <div id="myCarousel" class="carousel slide" data-ride="carousel">
                   <!-- Indicators -->
                   <ol class="carousel-indicators">
                     <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                     <li data-target="#myCarousel" data-slide-to="1"></li>
                     <li data-target="#myCarousel" data-slide-to="2"></li>
                     <li data-target="#myCarousel" data-slide-to="3"></li>
                     <li data-target="#myCarousel" data-slide-to="4"></li>
                     <li data-target="#myCarousel" data-slide-to="5"></li>
                     <li data-target="#myCarousel" data-slide-to="6"></li>
                     <li data-target="#myCarousel" data-slide-to="7"></li>
                   </ol>
               
                   <!-- Wrapper for slides -->
                   <div class="carousel-inner">
                     <div class="item active">
                       <img src="\\static\\img\\1.jpg" style="width:100%;">
                     </div>
               
                     <div class="item">
                       <img src="\\static\\img\\2.jpg" style="width:100%;">
                     </div>
                   
                     <div class="item">
                       <img src="\\static\\img\\3.jpg" style="width:100%;">
                     </div>
                     
                     <div class="item">
                       <img src="\\static\\img\\4.jpg" style="width:100%;">
                     </div>
                     
                     <div class="item">
                       <img src="\\static\\img\\5.jpg" style="width:100%;">
                     </div>
                     
                     <div class="item">
                       <img src="\\static\\img\\6.jpg" style="width:100%;">
                     </div>

                     <div class="item">
                       <img src="\\static\\img\\7.jpg" style="width:100%;">
                     </div>

                     <div class="item">
                       <img src="\\static\\img\\8.jpg" style="width:100%;">
                     </div>
                   </div>
               
                   <!-- Left and right controls -->
                   <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                     <span class="glyphicon glyphicon-chevron-left"></span>
                     <span class="sr-only">Previous</span>
                   </a>
                   <a class="right carousel-control" href="#myCarousel" data-slide="next">
                     <span class="glyphicon glyphicon-chevron-right"></span>
                     <span class="sr-only">Next</span>
                   </a>
                 </div>
               </div>
               
               </body>
               </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')