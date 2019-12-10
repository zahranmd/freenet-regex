# regexes
ALL = r'((((127.0.0.1|localhost):8888/){0,1}(freenet:){0,1}(USK|SSK|CHK)@[a-zA-Z0-9~\-]{43},[a-zA-Z0-9~\-]{43},(AQACAAE|AQABAAE|AQECAAE|AAMC--8|AAIC--8)/[a-zA-Z0-9\-\._%?\\& ]{0,150})/?[0-9\-]{0,10})/?(.*)'
USK = r'((((127.0.0.1|localhost):8888/){0,1}(freenet:){0,1}(USK)@[a-zA-Z0-9~\-]{43},[a-zA-Z0-9~\-]{43},(AQACAAE|AQABAAE|AQECAAE)/[a-zA-Z0-9\-\._%?\\& ]{0,150})/?[0-9\-]{0,10})/?(.*)'
SSK = r'((((127.0.0.1|localhost):8888/){0,1}(freenet:){0,1}(SSK)@[a-zA-Z0-9~\-]{43},[a-zA-Z0-9~\-]{43},(AQACAAE|AQABAAE|AQECAAE)/[a-zA-Z0-9\-\._%?\\& ]{0,150})/?[0-9\-]{0,10})/?(.*)'
CHK = r'((((127.0.0.1|localhost):8888/){0,1}(freenet:){0,1}(CHK)@[a-zA-Z0-9~\-]{43},[a-zA-Z0-9~\-]{43},(AAMC--8|AAIC--8)/[a-zA-Z0-9\-\._%?\\& ]{0,150})/?[0-9\-]{0,10})/?(.*)'