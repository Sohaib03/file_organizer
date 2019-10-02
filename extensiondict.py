def getpath(extension):
    return extension_dict[extension]

extension_dict = {
    # No name
    'noname' : "Other/Uncategorized",
    # Audio
    '.aif'   : "Media/Audio",
    '.cda'   : "Media/Audio",
    '.mid'   : "Media/Audio",
    '.midi'  : "Media/Audio",
    '.mp3'   : "Media/Audio",
    '.mpa'   : "Media/Audio",
    '.ogg'   : "Media/Audio",
    '.wav'   : "Media/Audio",
    '.wma'   : "Media/Audio",
    '.wpl'   : "Media/Audio",
    '.m3u'   : "Media/Audio",
    '.vox'   : "Media/Audio",
    '.8svx'  : "Media/Audio",
	'.16svx' : "Media/Audio",
	'.aiff,' : "Media/Audio",
	'.au'    : "Media/Audio",
	'.bwf'   : "Media/Audio",
	'.cdda'  : "Media/Audio",
	'.raw'   : "Media/Audio",
	'.ra,'   : "Media/Audio",
	'.flac'  : "Media/Audio",
	'.la'    : "Media/Audio",
	'.pac'   : "Media/Audio",
	'.ape'   : "Media/Audio",
	'.ofr,'  : "Media/Audio",
	'.rka'   : "Media/Audio",
	'.shn'   : "Media/Audio",
	'.tak'   : "Media/Audio",
	'.thd'   : "Media/Audio",
	'.tta'   : "Media/Audio",
	'.wv'    : "Media/Audio",
	'.brstm' : "Media/Audio",
	'.dts,'  : "Media/Audio",
	'.ast'   : "Media/Audio",
	'.aw'    : "Media/Audio",
	'.psf'   : "Media/Audio",
	'.ac3'   : "Media/Audio",
	'.amr'   : "Media/Audio",
	'.mp1'   : "Media/Audio",
	'.mp2'   : "Media/Audio",
	'.mpeg'  : "Media/Audio",
	'.spx'   : "Media/Audio",
	'.gsm'   : "Media/Audio",
	'.aac'   : "Media/Audio",
	'.mpc'   : "Media/Audio",
	'.vqf'   : "Media/Audio",
	'.ots'   : "Media/Audio",
	'.swa'   : "Media/Audio",
	'.voc'   : "Media/Audio",
	'.dwd'   : "Media/Audio",
	'.smp'   : "Media/Audio",
	'.mod'   : "Media/Audio",
	'.mt2'   : "Media/Audio",
	'.s3m'   : "Media/Audio",
	'.xm'    : "Media/Audio",
	'.it'    : "Media/Audio",
	'.nsf'   : "Media/Audio",
	'.mid,'  : "Media/Audio",
	'.ftm'   : "Media/Audio",
	'.ly'    : "Media/Audio",
	'.mus,'  : "Media/Audio",
	'.mxl,'  : "Media/Audio",
	'.mscx,' : "Media/Audio",
	'.sib'   : "Media/Audio",
	'.niff'  : "Media/Audio",
	'.ptb'   : "Media/Audio",
	'.asf'   : "Media/Audio",
	'.cust'  : "Media/Audio",
	'.gym'   : "Media/Audio",
	'.jam'   : "Media/Audio",
	'.mng'   : "Media/Audio",
	'.rmj'   : "Media/Audio",
	'.sid'   : "Media/Audio",
	'.spc'   : "Media/Audio",
	'.txm'   : "Media/Audio",
	'.vgm'   : "Media/Audio",
	'.ym'    : "Media/Audio",
	'.pvd'   : "Media/Audio",
    # Audio Editing
    '.als'   : "Media/Audio_Editing",
	'.alc'   : "Media/Audio_Editing",
	'.alp'   : "Media/Audio_Editing",
	'.aup'   : "Media/Audio_Editing",
	'.band'  : "Media/Audio_Editing",
	'.cel'   : "Media/Audio_Editing",
	'.cpr'   : "Media/Audio_Editing",
	'.cwp'   : "Media/Audio_Editing",
	'.drm'   : "Media/Audio_Editing",
	'.dmkit' : "Media/Audio_Editing",
	'.ens'   : "Media/Audio_Editing",
	'.flp'   : "Media/Audio_Editing",
	'.grir'  : "Media/Audio_Editing",
	'.logic' : "Media/Audio_Editing",
	'.mmr'   : "Media/Audio_Editing",
	'.mx6hs' : "Media/Audio_Editing",
	'.npr'   : "Media/Audio_Editing",
	'.omf,'  : "Media/Audio_Editing",
	'.rin'   : "Media/Audio_Editing",
	'.ses'   : "Media/Audio_Editing",
	'.sfl'   : "Media/Audio_Editing",
	'.sng'   : "Media/Audio_Editing",
	'.stf'   : "Media/Audio_Editing",
	'.snd'   : "Media/Audio_Editing",
	'.syn'   : "Media/Audio_Editing",
	'.vcls'  : "Media/Audio_Editing",
	'.vsq'   : "Media/Audio_Editing",
	'.vsqx'  : "Media/Audio_Editing",

    # Encrypted
    '.axx'  : "Other/Encrypted",
	'.eea'  : "Other/Encrypted",
	'.tc'   : "Other/Encrypted",
	'.kode' : "Other/Encrypted",


    # Text
    '.txt'   : "Text/TextFiles",
    '.doc'   : "Text/Word",
    '.docx'  : "Text/Word",
    '.odt'   : "Text/Word",
	'.gdoc'  : "Text/Gdoc",
    '.pdf'   : "Text/PDF",
    '.rtf'   : "Text/TextFiles",
    '.tex'   : "Text/TextFiles",
    '.wks'   : "Text/TextFiles",
    '.wps'   : "Text/TextFiles",
    '.wpd'   : "Text/TextFiles",
	'.epub'  : "Text/EPUB",
	'.mobi'  : "Text/mobi",
	'.log'   : "Text/logs",

	# Dot Files (Configuration files)
	'.conf'  :  "Text/DotFiles",
	'.gitignore' : "Text/DotFiles",
	'.vimsrc' : "Text/DotFiles",
	'.cfg'    : "Text/DotFiles",

    # Video
    '.3g2'   : "Media/Video",
    '.3gp'   : "Media/Video",
    '.avi'   : "Media/Video",
    '.flv'   : "Media/Video",
    '.h264'  : "Media/Video",
    '.m4v'   : "Media/Video",
    '.mkv'   : "Media/Video",
    '.mov'   : "Media/Video",
    '.mp4'   : "Media/Video",
    '.mpg'   : "Media/Video",
    '.mpeg'  : "Media/Video",
    '.rm'    : "Media/Video",
    '.swf'   : "Media/Video",
    '.vob'   : "Media/Video",
    '.wmv'   : "Media/Video",
    '.aaf'   : "Media/Video",
	'.gif'   : "Media/Video",
	'.asf'   : "Media/Video",
	'.avchd' : "Media/Video",
	'.bik'   : "Media/Video",
	'.cam'   : "Media/Video",
	'.collab': "Media/Video",
	'.dat'   : "Media/Video",
	'.dsh'   : "Media/Video",
	'.dvr-ms': "Media/Video",
	'.m1v'   : "Media/Video",
	'.m2v'   : "Media/Video",
	'.fla'   : "Media/Video",
	'.flr'   : "Media/Video",
	'.sol'   : "Media/Video",
	'.matroska': "Media/Video",
	'.wrap'  : "Media/Video",
	'.mng'   : "Media/Video",
	'.quicktime'  : "Media/Video",
	'.thp'   : "Media/Video",
	'.mxf'   : "Media/Video",
	'.roq'   : "Media/Video",
	'.nsv'   : "Media/Video",
	'.ogg'   : "Media/Video",
	'.svi'   : "Media/Video",
	'.smi'   : "Media/Video",
	'.smk'   : "Media/Video",
	'.wtv'   : "Media/Video",
	'.yuv'   : "Media/Video",
	'.webm'  : "Media/Video",
    
    #Video Editing and production
    '.braw'  : "Media/Video_Editing",
	'.fcp'   : "Media/Video_Editing",
	'.mswmm' : "Media/Video_Editing",
	'.ppj'   : "Media/Video_Editing",
	'.imovieproj'  : "Media/Video_Editing",
	'.veg'   : "Media/Video_Editing",
	'.suf'   : "Media/Video_Editing",
	'.wlmp'  : "Media/Video_Editing",
	'.kdenlive'  : "Media/Video_Editing",
	'.vpj'  : "Media/Video_Editing",
	'.motn' : "Media/Video_Editing",
	'.imoviemobile'  : "Media/Video_Editing",


    # Images
    '.ai'    : "Media/Images",
    '.bmp'   : "Media/Images",
    '.gif'   : "Media/Images",
    '.ico'   : "Media/Images",
    '.jpg'   : "Media/Images",
    '.jpeg'  : "Media/Images",
    '.png'   : "Media/Images",
    '.ps'    : "Media/Images",
    '.psd'   : "Media/Images",
    '.svg'   : "Media/Images",
    '.tif'   : "Media/Images",
    '.tiff'  : "Media/Images",
    '.CR2'   : "Media/Images",
    '.art'   : "Media/Images",
	'.blp'   : "Media/Images",
	'.bti'   : "Media/Images",
	'.cd5'   : "Media/Images",
	'.cit'   : "Media/Images",
	'.cpt'   : "Media/Images",
	'.cr2'   : "Media/Images",
	'.clip'  : "Media/Images",
	'.cpl'   : "Media/Images",
	'.dds'   : "Media/Images",
	'.dib'   : "Media/Images",
	'.djvu'  : "Media/Images",
	'.egt'   : "Media/Images",
	'.exif'  : "Media/Images",
	'.grf'   : "Media/Images",
	'.icns'  : "Media/Images",
	'.iff'   : "Media/Images",
	'.jng'   : "Media/Images",
	'.jfif'  : "Media/Images",
	'.jp2'   : "Media/Images",
	'.jps'   : "Media/Images",
	'.lbm'   : "Media/Images",
	'.max'   : "Media/Images",
	'.miff'  : "Media/Images",
	'.mng'   : "Media/Images",
	'.msp'   : "Media/Images",
	'.nitf'  : "Media/Images",
	'.otb'   : "Media/Images",
	'.pbm'   : "Media/Images",
	'.pc1'   : "Media/Images",
	'.pc2'   : "Media/Images",
	'.pc3'   : "Media/Images",
	'.pcf'   : "Media/Images",
	'.pcx'   : "Media/Images",
	'.pdn'   : "Media/Images",
	'.pgm'   : "Media/Images",
	'.pi1'   : "Media/Images",
	'.pi2'   : "Media/Images",
	'.pi3'   : "Media/Images",
	'.pict,' : "Media/Images",
	'.pnm'   : "Media/Images",
	'.pns'   : "Media/Images",
	'.ppm'   : "Media/Images",
	'.psb'   : "Media/Images",
	'.psd,'  : "Media/Images",
	'.psp'   : "Media/Images",
	'.px'    : "Media/Images",
	'.pxm'   : "Media/Images",
	'.pxr'   : "Media/Images",
	'.qfx'   : "Media/Images",
	'.raw'   : "Media/Images",
	'.rle'   : "Media/Images",
	'.sct'   : "Media/Images",
	'.sgi,'  : "Media/Images",
	'.tga'   : "Media/Images",
	'.ep'    : "Media/Images",
	'.vtf'   : "Media/Images",
	'.xbm'   : "Media/Images",
	'.xcf'   : "Media/Images",
	'.xpm'   : "Media/Images",
	'.zif'   : "Media/Images",
	'.3dv'   : "Media/Images",
	'.amf'   : "Media/Images",
	'.awg'   : "Media/Images",
	'.cgm'   : "Media/Images",
	'.cdr'   : "Media/Images",
	'.cmx'   : "Media/Images",
	'.dp'    : "Media/Images",
	'.dxf'   : "Media/Images",
	'.e2d'   : "Media/Images",
	'.eps'   : "Media/Images",
	'.fs'    : "Media/Images",
	'.gbr'   : "Media/Images",
	'.odg'   : "Media/Images",
	'.stl'   : "Media/Images",
	'.vrml'  : "Media/Images",
	'.x3d'   : "Media/Images",
	'.scene' : "Media/Images",
	'.sxd'   : "Media/Images",
	'.v2d'   : "Media/Images",
	'.vdoc'  : "Media/Images",
	'.vsd'   : "Media/Images",
	'.vsdx'  : "Media/Images",
	'.vnd'   : "Media/Images",
	'.wmf'   : "Media/Images",
	'.emf'   : "Media/Images",
	'.xar'   : "Media/Images",

    # Internet
    '.asp'   : "Other/Internet",
    '.aspx'  : "Other/Internet",
    '.cer'   : "Other/Internet",
    '.cfm'   : "Other/Internet",
    '.cgi'   : "Other/Internet",
    '.pl'    : "Other/Internet",
    '.css'   : "Other/Internet",
    '.htm'   : "Other/Internet",
    '.js'    : "Other/Internet",
    '.jsp'   : "Other/Internet",
    '.part'  : "Other/Internet",
    '.php'   : "Other/Internet",
    '.rss'   : "Other/Internet",
    '.xhtml' : "Other/Internet",
    
    # Compressed
    '.7z'    : "Other/Compressed",
    '.arj'   : "Other/Compressed",
    '.deb'   : "Other/Compressed",
    '.pkg'   : "Other/Compressed",
    '.rar'   : "Other/Compressed",
    '.rpm'   : "Other/Compressed",
    '.gz'    : "Other/Compressed",
    '.xz'    : "Other/Compressed",
    '.z'     : "Other/Compressed",
    '.zip'   : "Other/Compressed",
    '.tgz'   : "Other/Compressed",
    # Disc
    '.bin'   : "Other/Disc",
    '.dmg'   : "Other/Disc",
    '.iso'   : "Other/Disc",
    '.toast' : "Other/Disc",
    '.vcd'   : "Other/Disc",
    # Database
    '.csv'   : "Programming/Database",
    '.dat'   : "Programming/Database",
    '.db'    : "Programming/Database",
    '.dbf'   : "Programming/Database",
    '.log'   : "Programming/Database",
    '.mdb'   : "Programming/Database",
    '.sav'   : "Programming/Database",
    '.sql'   : "Programming/Database",
    '.tar'   : "Programming/Database",
    '.xml'   : "Programming/Database",
    '.json'  : "Programming/Database",
    '.4db'   : "Programming/Database",
	'.4dd'   : "Programming/Database",
	'.4dindy': "Programming/Database",
	'.4dindx': "Programming/Database",
	'.4dr'   : "Programming/Database",
	'.accdb' : "Programming/Database",
	'.accde' : "Programming/Database",
	'.adt'   : "Programming/Database",
	'.apr'   : "Programming/Database",
	'.box'   : "Programming/Database",
	'.chml'  : "Programming/Database",
	'.daf'   : "Programming/Database",
	'.dta'   : "Programming/Database",
	'.egt'   : "Programming/Database",
	'.ess'   : "Programming/Database",
	'.eap'   : "Programming/Database",
	'.fdb'   : "Programming/Database",
	'.fp,'   : "Programming/Database",
	'.frm'   : "Programming/Database",
	'.gdb'   : "Programming/Database",
	'.gtable': "Programming/Database",
	'.kexi'  : "Programming/Database",
	'.kexic' : "Programming/Database",
	'.kexis' : "Programming/Database",
	'.ldb'   : "Programming/Database",
	'.mda'   : "Programming/Database",
	'.adp'   : "Programming/Database",
	'.mde'   : "Programming/Database",
	'.mdf'   : "Programming/Database",
	'.myd'   : "Programming/Database",
	'.myi'   : "Programming/Database",
	'.ncf'   : "Programming/Database",
	'.nsf'   : "Programming/Database",
	'.ntf'   : "Programming/Database",
	'.nv2'   : "Programming/Database",
	'.odb'   : "Programming/Database",
	'.ora'   : "Programming/Database",
	'.pcontact': "Programming/Database",
	'.pdb'   : "Programming/Database",
	'.pdi'   : "Programming/Database",
	'.pdx'   : "Programming/Database",
	'.prc'   : "Programming/Database",
	'.rec'   : "Programming/Database",
	'.rel'   : "Programming/Database",
	'.rin'   : "Programming/Database",
	'.sdb'   : "Programming/Database",
	'.sdf'   : "Programming/Database",
	'.sqlite': "Programming/Database",
	'.udl'   : "Programming/Database",
	'.wadata': "Programming/Database",
	'.waindx': "Programming/Database",
	'.wamodel': "Programming/Database",
	'.wajournal': "Programming/Database",
	'.wdb'   : "Programming/Database",
	'.wmdb'  : "Programming/Database",

    # Desktop Publishing
    '.ai'   : "Other/Desktop_Publishing",
	'.ave'  : "Other/Desktop_Publishing",
	'.cdr'  : "Other/Desktop_Publishing",
	'.chp'  : "Other/Desktop_Publishing",
	'.cpt'  : "Other/Desktop_Publishing",
	'.dtp'  : "Other/Desktop_Publishing",
	'.fm'   : "Other/Desktop_Publishing",
	'.gdraw': "Other/Desktop_Publishing",
	'.ildoc': "Other/Desktop_Publishing",
	'.indd' : "Other/Desktop_Publishing",
	'.mcf'  : "Other/Desktop_Publishing",
	'.pdf'  : "Other/Desktop_Publishing",
	'.pmd'  : "Other/Desktop_Publishing",
	'.ppp'  : "Other/Desktop_Publishing",
	'.psd'  : "Other/Desktop_Publishing",
	'.pub'  : "Other/Desktop_Publishing",
	'.qxd'  : "Other/Desktop_Publishing",
	'.sla'  : "Other/Desktop_Publishing",
	'.wfp'  : "Other/Desktop_Publishing",
	'.wlmp' : "Other/Desktop_Publishing",
	'.wve'  : "Other/Desktop_Publishing",
	'.xcf'  : "Other/Desktop_Publishing",

    # Executables
    '.apk'   : "Other/Executables",
    '.bat'   : "Other/Executables",
    '.com'   : "Other/Executables",
    '.exe'   : "Other/Executables",
    '.gadget': "Other/Executables",
    '.jar'   : "Other/Executables",
    '.wsf'   : "Other/Executables",
	'.8bf'   : "Other/Executables",
	'.a'     : "Other/Executables",
	'.a.out' : "Other/Executables",
	'.app'   : "Other/Executables",
	'.bac'   : "Other/Executables",
	'.bpl'   : "Other/Executables",
	'.bundle': "Other/Executables",
	'.dcu'   : "Other/Executables",
	'.class' : "Other/Executables",
	'.coff'  : "Other/Executables",
	'.dll'   : "Other/Executables",
	'.dol'   : "Other/Executables",
	'.ear'   : "Other/Executables",
	'.elf'   : "Other/Executables",
	'.expander'  : "Other/Executables",
	'.o'     : "Other/Executables",
	'.obb'   : "Other/Executables",
	'.pif'   : "Other/Executables",
	'.s1es'  : "Other/Executables",
	'.so'    : "Other/Executables",
	'.vap'   : "Other/Executables",
	'.dos'   : "Other/Executables",
	'.ipa'   : "Other/Executables",
	'.jeff'  : "Other/Executables",
	'.xpi'   : "Other/Executables",
	'.mach-o': "Other/Executables",
	'.war'   : "Other/Executables",
	'.xbe'   : "Other/Executables",
	'.xap'   : "Other/Executables",
	'.xcoff' : "Other/Executables",
	'.vbx'   : "Other/Executables",
	'.ocx'   : "Other/Executables",
	'.tlb'   : "Other/Executables",

    # Fonts
    '.fnt'   : "Other/Fonts",
    '.fon'   : "Other/Fonts",
    '.otf'   : "Other/Fonts",
    '.ttf'   : "Other/Fonts",
    '.abf'   : "Other/Fonts",
	'.afm'   : "Other/Fonts",
	'.bdf'   : "Other/Fonts",
	'.bmf'   : "Other/Fonts",
	'.mgf'   : "Other/Fonts",
	'.pcf'   : "Other/Fonts",
	'.postscript'  : "Other/Fonts",
	'.pfa'   : "Other/Fonts",
	'.pfb'   : "Other/Fonts",
	'.pfm'   : "Other/Fonts",
	'.fond'  : "Other/Fonts",
	'.sfd'   : "Other/Fonts",
	'.snf'   : "Other/Fonts",
	'.tdf'   : "Other/Fonts",
	'.tfm'   : "Other/Fonts",
	'.ufo'   : "Other/Fonts",
	'.woff'  : "Other/Fonts",
    # Playlist formats
    '.aimppl': "Media/Playlist",
	'.asx'   : "Media/Playlist",
	'.ram'   : "Media/Playlist",
	'.xpl'   : "Media/Playlist",
	'.xspf'  : "Media/Playlist",
	'.zpl'   : "Media/Playlist",
	'.m3u'   : "Media/Playlist",
	'.pls'   : "Media/Playlist",


    # Presentations
    '.key'   : "Text/Presentations",
    '.odp'   : "Text/Presentations",
    '.pps'   : "Text/Presentations",
    '.ppt'   : "Text/Presentations",
    '.pptx'  : "Text/Presentations",
    '.gslides': "Text/Presentations",
	'.key,'  : "Text/Presentations",
	'.nb'    : "Text/Presentations",
	'.nbp'   : "Text/Presentations",
	'.otp'   : "Text/Presentations",
	'.pez'   : "Text/Presentations",
	'.pot'   : "Text/Presentations",
	'.prz'   : "Text/Presentations",
	'.sdd'   : "Text/Presentations",
	'.shf'   : "Text/Presentations",
	'.show'  : "Text/Presentations",
	'.shw'   : "Text/Presentations",
	'.slp'   : "Text/Presentations",
	'.sspss' : "Text/Presentations",
	'.sti'   : "Text/Presentations",
	'.sxi'   : "Text/Presentations",
	'.thmx'  : "Text/Presentations",
	'.watch' : "Text/Presentations",

    # Programming
    '.c'     : "Programming/C++andC",
    '.class' : "Programming/Java",
    '.cpp'   : "Programming/C++andC",
    '.dart'  : "Programming/Dart",
    '.h'     : "Programming/C++andC",
    '.html'  : "Programming/HTML",
    '.java'  : "Programming/Java",
    '.lua'   : "Programming/LUA",
    '.m'     : "Programming/MATLAB",
    '.py'    : "Programming/Python",
    '.sh'    : "Programming/Shell",
    '.swift' : "Programming/Swift",
	'.adb'   : "Programming/ada",
	'.ads'   : "Programming/ada",
	'.ahk'   : "Programming/autohotkey",
	'.applescript-'  : "Programming/AppleScript",
	'.as'    : "Programming/adobe",
	'.au3'   : "Programming/autoit",
	'.bat'   : "Programming/batch",
	'.bas'   : "Programming/qbasic",
	'.cljs'  : "Programming/clojurescript",
	'.cmd'   : "Programming/batch",
	'.coffee': "Programming/coffeescript",
	'.ino'   : "Programming/arduino",
	'.egg'   : "Programming/chicken",
	'.egt'   : "Programming/egt",
	'.erb'   : "Programming/embedded",
	'.hta'   : "Programming/html",
	'.ibi'   : "Programming/icarus",
	'.ici'   : "Programming/ici",
	'.ijs'   : "Programming/j_script",
	'.ipynb' : "Programming/ipython",
	'.itcl'  : "Programming/itcl",
	'.js'    : "Programming/javascript",
	'.jsfl'  : "Programming/adobe",
	'.lua'   : "Programming/lua",
	'.m'     : "Programming/mathematica",
	'.mrc'   : "Programming/mirc",
	'.ncf'   : "Programming/netware",
	'.nuc'   : "Programming/compiled",
	'.nud'   : "Programming/c++",
	'.nut'   : "Programming/squirrel",
	'.pde'   : "Programming/processing",
	'.php'   : "Programming/php",
	'.php?'  : "Programming/php", # ? = version number
	'.pl'    : "Programming/perl",
	'.pm'    : "Programming/perl",
	'.ps1'   : "Programming/windows_powershell",
	'.ps1xml': "Programming/windows_powershell",
	'.psc1'  : "Programming/windows_powershell",
	'.psd1'  : "Programming/windows_poweshell",
	'.psm1'  : "Programming/windows_powershell",
	'.py'    : "Programming/python",
	'.pyc'   : "Programming/python",
	'.pyo'   : "Programming/python",
	'.r'     : "Programming/r",
	'.r'     : "Programming/rebol",
	'.rb'    : "Programming/ruby",
	'.rdp'   : "Programming/rdp",
	'.red'   : "Programming/red",
	'.rs'    : "Programming/rust",
	'.sb2'   : "Programming/scratch",
	'.scpt'  : "Programming/applescript",
	'.scptd' : "Programming/SCPTD",
	'.sdl'   : "Programming/SDL",
	'.sh'    : "Programming/shell",
	'.syjs'  : "Programming/symat",
	'.sypy'  : "Programming/symat",
	'.tcl'   : "Programming/tcl",
	'.tns'   : "Programming/ti-nspire",
	'.vbs'   : "Programming/visual",
	'.xpl'   : "Programming/xproc",
	'.ebuild': "Programming/gentoo",

    # Spreadsheets
    '.ods'   : "Text/Spreadsheets",
    '.xlr'   : "Text/Spreadsheets",
    '.xls'   : "Text/Spreadsheets",
    '.xlsx'  : "Text/Spreadsheets",
    '.123'   : "Text/Spreadsheets",
	'.ab2'   : "Text/Spreadsheets",
	'.ab3'   : "Text/Spreadsheets",
	'.aws'   : "Text/Spreadsheets",
	'.bcsv'  : "Text/Spreadsheets",
	'.clf'   : "Text/Spreadsheets",
	'.cell'  : "Text/Spreadsheets",
	'.csv'   : "Text/Spreadsheets",
	'.gsheet': "Text/Spreadsheets",
	'.numbers': "Text/Spreadsheets",
	'.gnumeric': "Text/Spreadsheets",
	'.lcw'   : "Text/Spreadsheets",
	'.ots'   : "Text/Spreadsheets",
	'.qpw'   : "Text/Spreadsheets",
	'.sdc'   : "Text/Spreadsheets",
	'.slk'   : "Text/Spreadsheets",
	'.stc'   : "Text/Spreadsheets",
	'.sxc'   : "Text/Spreadsheets",
	'.tab'   : "Text/Spreadsheets",
	'.txt'   : "Text/Spreadsheets",
	'.vc'    : "Text/Spreadsheets",
	'.wk1'   : "Text/Spreadsheets",
	'.wk3'   : "Text/Spreadsheets",
	'.wk4'   : "Text/Spreadsheets",
	'.wks'   : "Text/Spreadsheets",
	'.wq1'   : "Text/Spreadsheets",
	'.xlk'   : "Text/Spreadsheets",
	'.xlsb'  : "Text/Spreadsheets",
	'.xlsm'  : "Text/Spreadsheets",
	'.xlt'   : "Text/Spreadsheets",
	'.xltm'  : "Text/Spreadsheets",
	'.xlw'   : "Text/Spreadsheets",

    # System
    '.bak'   : "Text/Other/System",
    '.cab'   : "Text/Other/System",
    '.cfg'   : "Text/Other/System",
    '.cpl'   : "Text/Other/System",
    '.cur'   : "Text/Other/System",
    '.dll'   : "Text/Other/System",
    '.dmp'   : "Text/Other/System",
    '.drv'   : "Text/Other/System",
    '.icns'  : "Text/Other/System",
    '.ini'   : "Text/Other/System",
    '.lnk'   : "Text/Other/System",
    '.msi'   : "Text/Other/System",
    '.sys'   : "Text/Other/System",
    '.tmp'   : "Text/Other/System",

	# Virtual Machines 
	'.vfd'  : "Other/VMs",
	'.vhd'  : "Other/VMs",
	'.vud'  : "Other/VMs",
	'.vmc'  : "Other/VMs",
	'.vsv'  : "Other/VMs",
	'.log'  : "Other/VMs",
	'.vmdk,': "Other/VMs",
	'.nvram': "Other/VMs",
	'.vmem' : "Other/VMs",
	'.vmsd' : "Other/VMs",
	'.vmsn' : "Other/VMs",
	'.vmss,std'  : "Other/VMs",
	'.vmtm'  : "Other/VMs",
	'.vmx,cfg'  : "Other/VMs",
	'.vmxf'  : "Other/VMs",
	'.vdi'   : "Other/VMs",
	'.vbox-extpack'  : "Other/VMs",
	'.hdd'   : "Other/VMs",
	'.pvs'   : "Other/VMs",
	'.sav'   : "Other/VMs",
	'.cow'   : "Other/VMs",
	'.qcow'  : "Other/VMs",
	'.qcow2' : "Other/VMs",
	'.qed'   : "Other/VMs",

}
