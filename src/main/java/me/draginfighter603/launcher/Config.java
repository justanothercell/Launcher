package me.draginfighter603.launcher;

import org.json.JSONObject;

import javax.swing.*;
import java.io.*;

public class Config {
    public static final String BASE_URL = "https://dragonfighter603.eu.pythonanywhere.com";

    public static String getOrDemandUserToken(){
        JSONObject config = loadConfig();
        String token = null;
        if(config.has("token")) token = config.getString("token");
        if(token == null) token = JOptionPane.showInputDialog(null, "Please enter your user token", "Enter user token", JOptionPane.INFORMATION_MESSAGE).trim();
        if(token == null) System.exit(0);
        while (!isTokenValid(token)){
            token = JOptionPane.showInputDialog(null, "The provided token was invalid.\nPlease enter your user token", "Enter user token", JOptionPane.INFORMATION_MESSAGE).trim();
            if(token == null) System.exit(0);
        }
        config.put("token", token);
        saveConfig(config);
        return token;
    }

    public static boolean isTokenValid(String token){
        return Http.jsonHttpGet(BASE_URL+"/verify?id="+token).getBoolean("success");
    }

    private static JSONObject loadConfig(){
        File config = new File("data/config.json");
        if(!config.exists()) return new JSONObject();
        try(BufferedReader fileReader = new BufferedReader(new InputStreamReader(new FileInputStream("data/config.json")))) {
            StringBuilder resultStringBuilder = new StringBuilder();
            String line;
            while ((line = fileReader.readLine()) != null) {
                resultStringBuilder.append(line).append("\n");
            }
            return new JSONObject(resultStringBuilder.toString());
        } catch (IOException e) {
            Helper.showException(e);
        }
        return new JSONObject();
    }

    private static void saveConfig(JSONObject json){
        new File("data").mkdirs();
        try(FileWriter fileWriter = new FileWriter("data/config.json")) {
            String fileContent = "This is a sample text.";
            fileWriter.write(json.toString(4));
        } catch (IOException e) {
            Helper.showException(e);
        }
    }
}
