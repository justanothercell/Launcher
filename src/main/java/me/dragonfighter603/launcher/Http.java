package me.dragonfighter603.launcher;

import org.apache.http.HttpRequest;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;

public class Http {

    public static JSONObject jsonHttpGet(String url){
        try {
            HttpGet http = new HttpGet(url);
            CloseableHttpClient httpClient = HttpClients.createDefault();
            HttpResponse response = httpClient.execute(http);
            StringBuilder data = new StringBuilder();
            InputStream stream = response.getEntity().getContent();
            int inByte;
            while ((inByte = stream.read()) != -1){
                data.append((char) inByte);
            }
            return new JSONObject(data.toString());
        } catch (IOException e) {
            return new JSONObject("{\"success\": false}");
        }
    }
}
