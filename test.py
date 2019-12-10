from find_freenet_regex import *

# text = ''' this is a freenet regex example 
# for 3 types of freesites localhost:8888/freenet:USK@Yj~Dkmu9Mat2XJniUE~QfKiHosSZB6DXvEJ7ePll17c,AqcVLD4MoGQIZ3TSGXZuuswl03GwF186qoTE~woXL1E,AQACAAE/IKE/3  
# localhost:8888/freenet:SSK@LZW~Vc-emLj35RqZ4nljxWzKOZxqTys7Gg-RP889uDM,z-EUdr9bREg6i3-06skcLxkazQhWUxHV49fkkdkAB-U,AQACAAE/JenniferLoveHewitt-1
# 127.0.0.1:8888/freenet:CHK@t~AG2wiOl7SUhU0~8bFL9-0Pq~9xPE7a0zEygpooHYE,chq8J3vV-vu7GqZUdHN6y5mVxadQmBcui-xYl7DeW94,AAIC--8/Fushchich%2C Nikitin. Symmetry of equations of quantum mechanics%28478s%29.pdf
			
# '''


# html = '''
# <html>
#     <head>
#         <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
#         <title>Freenet</title>
#         <link rel="stylesheet" href="/static/themes/winterfacey/theme.css" type="text/css" title="winterfacey">
			
# 	</head>
#     <body id="page-_" class="fproxy-page">
#         <div id="page">
#             <div id="content">
#                     <div class="infobox-header">
#                         Error: Data not found
#                     </div>
                    
#                 </div>
#                 <div class="infobox infobox-error">
#                     <div class="infobox-content">
#                         <p>Freenet was unable to retrieve this file.</p><p>The request was terminated by a node because it had recently received a request for the same key and that request had failed</p>
#                     </div>
#                         <ul>
#                             <li><a href="/freenet:USK@fZJH1Ps03jbBwM3Xuyn1YSTrhUu61EWCcZZcFL0-qeQ,SYbkVkROwzX7O-sSNqjZoLLrLd4xe9V6qn1pQws8HE8,AQACAAE/celery/127/files/">Retry now</a></li>
#                             <li><a href="https://localhost:8888/freenet:SSK@LZW~Vc-emLj35RqZ4nljxWzKOZxqTys7Gg-RP889uDM,z-EUdr9bREg6i3-06skcLxkazQhWUxHV49fkkdkAB-U,AQACAAE/JenniferLoveHewitt-1" title="Go back to the previous page">Go back to the previous page</a></li>
#                             <li><a href="localhost:8888/freenet:CHK@t~AG2wiOl7SUhU0~8bFL9-0Pq~9xPE7a0zEygpooHYE,chq8J3vV-vu7GqZUdHN6y5mVxadQmBcui-xYl7DeW94,AAIC--8/Fushchich%2C Nikitin. Symmetry of equations of quantum mechanics%28478s%29.pdf" title="Go back to the previous page">Go back to the previous page</a></li>
#                         </ul>
                        
#                     </div>
                    
#                 </div>
                
#             </div>
#     </body></html>
# '''


# uri = "127.0.0.1:8888/freenet:USK@qd-hk0vHYg7YvK2BQsJMcUD5QSF0tDkgnnF6lnWUH0g,xTFOV9ddCQQk6vQ6G~jfL6IzRUgmfMcZJ6nuySu~NUc,AQACAAE/activelink-index/125"
# uri = "localhost:8888/freenet:CHK@xV66vYABcehPGkVGxngKdnqIuT3cSDfxIG1nHZmI7sY,yqdshl52v1ZSKti05V7PbXwgURmsca3IqGCVVQYZ9Dw,AAIC--8/Christofides %28ed.%29. Combinatorial optimization %28Wiley%2C 1978%29%28L%29%28T%29%28212s%29.djvu"
# uri = "localhost:8888/freenet:SSK@LZW~Vc-emLj35RqZ4nljxWzKOZxqTys7Gg-RP889uDM,z-EUdr9bREg6i3-06skcLxkazQhWUxHV49fkkdkAB-U,AQACAAE/JenniferLoveHewitt-1"


# pass type as initial variable of class
# type = ALL or USK or SSK or CHK
free_ins = freenet("ALL")

# res = free_ins.extract_from_text(text)
# res = free_ins.extract_from_html(html)
# res = free_ins.check(uri)
# print(res)