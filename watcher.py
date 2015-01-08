import re
import urllib

# All current Curricula: http://tugbox.herokuapp.com/tug/curricula.html:
# Info Bakk 10u:   http://tugbox.herokuapp.com/tug/curriculum/557,140,1034/exams.html
# Info Bakk 14U:   http://tugbox.herokuapp.com/tug/curriculum/632,140,1035/exams.html
# Info Master 14U: http://tugbox.herokuapp.com/tug/curriculum/631,305,1035/exams.html

watchlist = ["Klassische Themen der Computerwissenschaft", "Entwurf und Analyse von Algorithmen", "Geometrische Algorithmen"]

site = urllib.urlopen("http://tugbox.herokuapp.com/tug/curriculum/557,140,1034/exams.html")
data = site.read()

pattern1 = re.compile(r"""
		<tr class="exam default">\s* 
              <td>03.07.2015</td>\s* 
              <td>([A-Za-z\s]*)</td>\s* 
              <td class="visible-lg"><kbd>([A-Za-z0-9\s\.]*)</kbd></td>\s* 
              <td><kbd>([A-Za-z0-9\s]*)</kbd></td>\s* 
              <td><a href=\"([^\"]*)\">([A-Za-z0-9\-\s]*)</a> <i title=\"External Link\" class=\"icon-external-link\"></i> </td>\s*
              <td>([0-9:]*)</td>\s* 
              <td>([0-9:]*)</td>\s* 
              <td class="visible-lg">([0-9:\.\s]*)</td>\s* 
              <td class="hidden-sm hidden-xs">([0-9:\.\s]*)</td>\s* 
              <td class="text-right">\s* 
                <a class="ical icon-calendar" href="(/tug/courses/[0-9]*/exams.ical)"></a>\s* 
                &nbsp;\s* 
                <a class="ical icon-rss" href="(webcal://tugbox.herokuapp.com/tug/courses/[0-9]*/exams.ical)"></a>\s* 
              </td>\s* 
            </tr>
	""", re.DOTALL | re.IGNORECASE | re.MULTILINE)

pattern2 = re.compile(r'<td><a href=\"([^\"]*)\">([A-Za-z0-9\-\s]*)</a> <i title=\"External Link\" class=\"icon-external-link\"></i> </td>', re.DOTALL | re.IGNORECASE | re.MULTILINE)

for match in pattern2.finditer(data):
	lvurl = match.group(1)
	lvname = match.group(2)

	if lvname in watchlist:
		print lvname, "-> ", lvurl

