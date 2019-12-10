# freenet-regex
extract and recognize Freenet sites (Freesites)


Introduction to Freenet and Freesites:
Freenet is free software which lets you anonymously share files, browse and publish "Freesites" (web sites accessible only through Freenet) and chat on forums, without fear of censorship. Freenet is decentralized to make it less vulnerable to attack.

Freesites:
Browsing user's Freesites are a popular way of using Freenet. Freesites are static websites that reside inside the Freenet network, and are only accessible through the Freenet network. 

Freenet keys:
Each file that exists on Freenet has a key associated with it. Freenet has various types of keys. Keys are used for everything on Freenet, and are a kind of URI.

Accessing data:
To access a particular piece of data on Freenet, you need to know the key to the data, and enter it like this (or click a link containing the key):
http://localhost:8888/[Freenet Key]    /    http://127.0.0.1:8888/[Freenet Key]

These are three mostly used keys in Freenet:
•	CHK - Content Hash Keys
•	SSK - Signed Subspace Keys
•	USK - Updatable Subspace Keys

Content Hash Keys (CHK):
Content Hash Keys(CHKs) are for files with static content, like an .mp3 or a PDF-document. These keys are hashes of the content of the file. A hash is a reproducible method of turning a specific piece of data into a relatively small number that serve as a sort of fingerprint for the data. If the file content changes, even ever so little, the hash of the file changes radically. A CHK uniquely identifies a file, it should not be possible for two files with different content to have the same CHK. The CHK consists of three parts:
•	the hash for the file
•	the decryption key that unlocks the file
•	the cryptographic settings
So, a typical CHK key looks like this:
CHK @ file hash, decryption key, crypto settings
For example:
localhost:8888/freenet:CHK@MBkDVZUDgjVN4Hrjtj8u2~KBtAXGzJGte99CRhA-TZU,q4dp0VskEeY9lC1OHJTq-~TDX32q37oOX8BpvDMWrdQ,AAIC--8/Zeh.Arrow of time%28draft%29%28230s%29.pdf
In the example, the above mentioned parts of CHK are: 
•	MBkDVZUDgjVN4Hrjtj8u2~KBtAXGzJGte99CRhA-TZU, file hash
•	q4dp0VskEeY9lC1OHJTq-~TDX32q37oOX8BpvDMWrdQ, decryption key
•	AAIC—8, crypto settings
•	Arrow of time %28draft%29%28230s%29.pdf, file name 

Signed Subspace Keys (SSKs):
Signed Subspace Keys (SSKs) are usually for sites that are going to change over time. For example, a website that may need news to be updated or information to be corrected, added or deleted. They work in such a way that someone else can't put up a newer version of your site and pretend it was you who did it. It works by using public-key cryptography so you automatically sign your site. Only the person with the secret key can add updated versions of your site to Freenet.
Here's an example of an address of a real SSK site in Freenet:
localhost:8888/freenet:SSK@spOnEa2YvAoNfreZPfoy0tVNCzQghLdWaaNM10GEiEM,QRKjyaBkOX5Qw~aEml19WIDaJJo2X3hU9mGz8GcUuKc,AQACAAE/freesite_es-1
•	spOnEa2YvAoNfreZPfoy0tVNCzQghLdWaaNM10GEiEM, is the hash of the public key. This part is all that is required to uniquely identify the file.
•	QRKjyaBkOX5Qw~aEml19WIDaJJo2X3hU9mGz8GcUuKc, is the document decryption key. 
•	AQACAAE is the encryption settings
•	freesite_es-1, is a word chosen by the site creator, and the 1 is the version of the site. The version number is incremented each time you create a new version of the site and insert it into Freenet.

Updateable Subspace Keys (USKs):
Updateable Subspace Keys (USKs) are useful for linking to the latest version of a Signed Subspace Key site. Note that USKs are really just a user-friendly wrapper around SSKs, which hide the process of searching for more recent versions of a site. There are two types of USK addresses:
You can have a USK address with a positive number at the end, like this:
•	http://127.0.0.1:8888/USK@rd0SN1...ABAAE/mysite/5/
The other type of USK address has a negative number at the end, like this:
•	http://127.0.0.1:8888/USK@rd0SN1...ABAAE/mysite/-7/
For both types of USKs, the address in the browser address bar will be changed to the positive number of the most recent version they have found.
Here's an example of an address of a real USK site in Freenet:
localhost:8888/freenet:USK@AdBE0xOQQMktD0mFZ0pY5mloVUxe-jlMx0aZQqc7jtY,KzlYqqEPd9VQ6n8qXFxIUUKzB5v2WEXo4bG7V5nSR6Q,AQACAAE/FreeBook/13
•	AdBE0xOQQMktD0mFZ0pY5mloVUxe-jlMx0aZQqc7jtY, is the hash of the public key
•	KzlYqqEPd9VQ6n8qXFxIUUKzB5v2WEXo4bG7V5nSR6Q, is the decryption key
•	AQACAAE, is the encryption settings
•	FreeBook, name of site chosen by user
•	13, version of site

Prerequisites:
•	Python 
•	pip3 (or just pip for python 2.7)

Installing: 
•	pip install bs4
•	pip install lxml
•	pip install regex

Note: If these commands do not work, try them with pip3.


How to use: 
  In this project, we have find_freenet_regex.py file in which we define different cases for detecting and extracting freesite’s links. It is possible to detect and extract a freesite from text and html file. Also, you can test an URL to see if it is a valid freesite or not.
For this, you should call the related function (extract_from_text/ extract_from_html / check) which is defined in find_freenet_regex.py. 
Beside, you can determine the type of your desired freesite key. This parameter can be ‘USK’, ‘SSK’, ‘CHK’ and ‘ALL’. If you set ‘ALL’, you can extract any key type of freesites. 
For better understanding, there is a test.py file, in which you can see some examples. Suppose that you have a text file and you want to see if there is any valid freesite address in your text or not. You should call “extract_from_text” and pass a text. For this, uncomment the text file in test.py and also call related function to extract keys from the text. Here it is: 
•	res = free_ins.extract_from_text(text). 
Also, you can determine the key type by free_ins. For example, ‘free_ins = freenet("USK")’ means that you are interested to extract just ‘USK’ addresses from the given text file. As mentioned above, this parameter can be ALL, USK, SSK and CHK. 

Contributing:
If you are missing a feature or have a new idea, go for it! That is what open-source is for!

Authors:
Zahra Niroumand (@zahranmd)
Morita Tarverdians (@mtarverdians)
