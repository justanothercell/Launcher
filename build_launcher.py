import json
import shutil
from jinja2 import Template

shutil.copy('pom.xml', 'pom.copy.xml')


# "-Dmaven.multiModuleProjectDirectory=D:\Files\Coding\Java\Intellij\Launcher Project\Launcher" "-Dmaven.home=C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\plugins\maven\lib\maven3" "-Dclassworlds.conf=C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\plugins\maven\lib\maven3\bin\m2.conf" "-Dmaven.ext.class.path=C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\plugins\maven\lib\maven-event-listener.jar" "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\lib\idea_rt.jar=65485:C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\plugins\maven\lib\maven3\boot\plexus-classworlds-2.6.0.jar;C:\Program Files\JetBrains\IntelliJ IDEA 2021.3.2\plugins\maven\lib\maven3\boot\plexus-classworlds.license" org.codehaus.classworlds.Launcher -Didea.version=2021.3.3 package
with open('config.json') as config_json:
    config = json.load(config_json)

with open('pom.copy.xml', 'r') as pom_read:
    pom = pom_read.read()
    with open('pom.xml', 'w'):
        pomtlate = Template(pom)
        msg = pomtlate.render(launcher_name="Test Launcher", launcher_title="TestLauncher")

