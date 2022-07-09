import json
import os
import shutil
import traceback

from jinja2 import Template


def build():
    exep = None
    try:
        print('=== Building Installer ===')
        print()
        os.chdir('Launcher')

        print('Loading config.json')
        with open('config.json') as config_json:
            config = json.load(config_json)
        try:
            launcher_config = config['launcher']
            java_path = config['java_path']
            launcher_name = launcher_config['name']
            launcher_title = launcher_config['name']
            icon_png = launcher_config['icon_png']
            icon_ico = launcher_config['icon_ico']
        except KeyError as e:
            print('Error while loading config.json:')
            print(f'Expected key {e}')
            print('Aborting!')
            raise e
        print()

        print('Copying resources')
        shutil.copy('../'+icon_png, 'src/main/resources/icon.png')
        shutil.copy('../'+icon_ico, 'src/main/resources/icon.ico')
        # setup pom
        print('Setting up pom.xml with variables')
        print('Copying pom.xml to pom.copy.mxl for later reset')
        shutil.copy('pom.xml', 'pom.copy.xml')
        with open('pom.copy.xml', 'r') as pom_read:
            pom = pom_read.read()
            with open('pom.xml', 'w') as pom_write:
                pomtlate = Template(pom)
                pom_rendered = pomtlate.render(launcher_name=launcher_name, launcher_title=launcher_title)
                pom_write.write(pom_rendered)
        print()

        print('Running launcher build')
        os.system(' '.join([java_path,
                  '"-Dmaven.multiModuleProjectDirectory=D:\\Files\\Coding\\Java\\Intellij\\Launcher Project\\Launcher"',
                  '"-Dmaven.home=C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\plugins\\maven\\lib\\maven3"',
                  '"-Dclassworlds.conf=C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\plugins\\maven\\lib\\maven3\\bin\\m2.conf"',
                  '"-Dmaven.ext.class.path=C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\plugins\\maven\\lib\\maven-event-listener.jar"',
                  '"-javaagent:C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\lib\\idea_rt.jar=65485:C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\bin"',
                  '-Dfile.encoding=UTF-8',
                  '-classpath "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\plugins\\maven\\lib\\maven3\\boot\\plexus-classworlds-2.6.0.jar;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.2\\plugins\\maven\\lib\\maven3\\boot\\plexus-classworlds.license"',
                  'org.codehaus.classworlds.Launcher -Didea.version=2021.3.3 package']))
        print('Finished launcher build successfully or unsuccessfully')
        print()
    except Exception as e:
        print()
        print('Aborting due to error:')
        print(repr(e))
        print(traceback.format_exc())
        print()
        exep = e
    finally:
        # reset pom
        if os.path.exists('pom.copy.xml'):
            print('Resetting by copying pom.copy.xml back to pom.mxl')
            shutil.copy('pom.copy.xml', 'pom.xml')
            print('Deleting and resetting...')
            os.remove('pom.copy.xml')
            os.remove('src/main/resources/icon.png')
            os.remove('src/main/resources/icon.ico')
            os.chdir('..')
            print()
        print('Finished!')
        if exep is None:
            return f'{launcher_name}.exe'
        else:
            raise exep


if __name__ == '__main__':
    build()