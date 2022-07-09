package me.dragonfighter603.launcher;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Data {
    private static JSONObject config;

    public static String get(String key){
        if(config == null){
            try {
                config = new JSONObject(String.join("\n",
                        Files.readAllLines(new File(Data.class.getClassLoader().getResource("data.json").getFile()).toPath())));
            } catch (IOException | JSONException ignored) {

            }
        }
        return config.getString(key);
    }
}
