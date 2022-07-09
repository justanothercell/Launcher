package me.dragonfighter603.launcher;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.util.Objects;
import java.util.Scanner;

public class Data {
    private static JSONObject config;

    public static String get(String key){
        if(config == null){
            try {
                InputStream stream = Objects.requireNonNull(Main.class.getClassLoader().getResourceAsStream("data.json"));
                config = new JSONObject(new Scanner(stream, "UTF-8").useDelimiter("\\A").next());
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
        return config.getString(key);
    }
}
