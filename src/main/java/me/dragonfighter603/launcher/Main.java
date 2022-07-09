package me.dragonfighter603.launcher;

import com.formdev.flatlaf.FlatDarkLaf;
import org.json.JSONObject;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Objects;

public class Main {
    public static void main(String[] args) {
        try {
            FlatDarkLaf.setup();

            File dataDir = new File("data");
            if (!dataDir.exists()) {
                dataDir.mkdir();
            }

            String action = "run";

            if (args.length > 0) action = args[args.length - 1];

            if (action.equals("run")) {
                run();
            } else if (action.equals("overrideLauncher")) {
                overrideLauncher();
            } else {
                Helper.showException(new IllegalArgumentException("Command line argument 1 " + action + "\ndoes not seem to be valid."));
                System.exit(1);
            }
        }
        catch (Exception e){
            Helper.showException(e);
            System.exit(1);
        }
    }

    public static void run(){
        Gui gui = new Gui();

        JFrame root = new JFrame(Data.get("title"));
        root.setContentPane(gui.mainPanel);
        root.setResizable(false);
        try {
            root.setIconImage(ImageIO.read(Objects.requireNonNull(Main.class.getClassLoader().getResourceAsStream("icon.png"))));
        } catch (IOException e) {
            e.printStackTrace();
        }
        root.setSize(600, 200);
        root.setVisible(true);
        root.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        gui.statusLabel.setText("Fetching data...");

        // === LAUNCHER UPDATE ===
        JSONObject launcherVersion = Http.jsonHttpGet(Data.get("server") + "/get_version?file=launcher");
        String ownLauncherVersion = "0.0.0";
        try (BufferedReader fileReader = new BufferedReader(new InputStreamReader(Objects.requireNonNull(Main.class.getClassLoader().getResourceAsStream("version"))))) {
            StringBuilder resultStringBuilder = new StringBuilder();
            String line;
            while ((line = fileReader.readLine()) != null) {
                resultStringBuilder.append(line).append("\n");
            }
            ownLauncherVersion = resultStringBuilder.toString();
        } catch (IOException e) {
            Helper.showException(e);
        }
        if (!ownLauncherVersion.trim().equals(launcherVersion.getString("version"))) {
            gui.statusLabel.setText("<html>Found launcher version to update!<br>" +
                    "(" + ownLauncherVersion + " -> " + launcherVersion.getString("version") + ")<br>" +
                    "Downloading...</html>");
            Downloader.download(Data.get("server") + "/download?file=launcher", "data/updater.exe", gui.progressBar);
            Runtime rt = Runtime.getRuntime();
            try {
                rt.exec("cmd /c data\\updater.exe overrideLauncher");
                System.exit(0);
            } catch (IOException e) {
                Helper.showException(e);
                System.exit(1);
            }
        }

        // === GAME UPDATE ===
        File af = new File("data/application");
        af.mkdirs();
        String applicationFolder = "0.0.0";
        for(String file : Objects.requireNonNull(af.list())) {
            applicationFolder = file;
        }
        JSONObject gameVersion = Http.jsonHttpGet(Data.get("server") + "/get_version?file=application");
        if (!applicationFolder.equals(gameVersion.getString("version"))) {
            gui.statusLabel.setText("<html>Found game version to update!<br>" +
                    "(" + applicationFolder + " -> " + gameVersion.getString("version") + ")<br>" +
                    "Downloading...</html>");
            purgeDirectory(new File("data/application"));
            gui.statusLabel.setText("<html>Found game version to update!<br>" +
                    "(" + applicationFolder + " -> " + gameVersion.getString("version") + ")<br>" +
                    "Downloading...</html>");
            Downloader.download(Data.get("server") + "/download?file=application", "data/application.zip", gui.progressBar);
            gui.statusLabel.setText("<html>Found game version to update!<br>" +
                    "(" + applicationFolder + " -> " + gameVersion.getString("version") + ")<br>" +
                    "Unzipping...</html>");
            Downloader.unzip("data/application.zip", "data/application", gui.progressBar);
            gui.statusLabel.setText("<html>Found game version to update!<br>" +
                    "(" + applicationFolder + " -> " + gameVersion.getString("version") + ")<br>" +
                    "finished!</html>");
            for(String file : Objects.requireNonNull(new File("data/application").list())) {
                applicationFolder = file;
            }
        }
        Runtime rt = Runtime.getRuntime();
        try {
            System.out.println("data\\application\\" + applicationFolder + "\\" + Data.get("application"));
            rt.exec("data\\application\\" + applicationFolder + "\\" + Data.get("application"));
            System.exit(0);
        } catch (IOException e) {
            Helper.showException(e);
            System.exit(1);
        }
    }

    public static void overrideLauncher(){
        try {
            Files.copy(Paths.get("data/updater.exe"), Paths.get("GladiatronLauncher.exe"), StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException e) {
            Helper.showException(e);
            System.exit(1);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e2) {
                e2.printStackTrace();
            }
        }
        Runtime rt = Runtime.getRuntime();
        try {
            rt.exec("cmd /c GladiatronLauncher.exe");
        } catch (IOException e) {
            Helper.showException(e);
            System.exit(1);
        }
        System.exit(0);
    }

    private static void purgeDirectory(File dir) {
        for (File file: Objects.requireNonNull(dir.listFiles())) {
            if (file.isDirectory())
                purgeDirectory(file);
            file.delete();
        }
    }
}
