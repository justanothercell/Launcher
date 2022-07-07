package me.draginfighter603.launcher;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

import javax.swing.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class Downloader {
    private static final int BUFFER_SIZE = 4096;

    public static void download(String url, String fileDest, JProgressBar progressBar){
        try {
            HttpGet httpget = new HttpGet(url);
            CloseableHttpClient httpClient = HttpClients.createDefault();
            HttpResponse response = httpClient.execute(httpget);
            int size = Integer.parseInt(response.getFirstHeader("Content-Length").getValue());
            HttpEntity entity = response.getEntity();
            BufferedInputStream bis = new BufferedInputStream(entity.getContent());
            BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(fileDest));
            int progress = 0;
            int inByte;
            while((inByte = bis.read()) != -1) {
                bos.write(inByte);
                progressBar.setValue((int)(progress/(float)size*1000));
                progress++;
            }
            bis.close();
            bos.close();
        } catch (IOException e) {
            Helper.showException(e);
        }
    }

    public static void unzip(String zipFilePath, String destDirectory, JProgressBar progressBar){
        try {
            File destDir = new File(destDirectory);

            if (!destDir.exists()) {
                destDir.mkdir();
            }
            long size = Files.size(Paths.get(zipFilePath));
            long extracted = 0;
            ZipInputStream zipIn = new ZipInputStream(new FileInputStream(zipFilePath));

            ZipEntry entry = zipIn.getNextEntry();
            // iterates over entries in the zip file
            while (entry != null) {
                String filePath = destDirectory + File.separator + entry.getName();
                if (!entry.isDirectory()) {
                    // if the entry is a file, extracts it
                    extractFile(zipIn, filePath);
                    extracted += entry.getCompressedSize();
                    progressBar.setValue((int)(extracted/(float)size*1000));
                } else {
                    // if the entry is a directory, make the directory
                    File dir = new File(filePath);
                    dir.mkdirs();
                }
                zipIn.closeEntry();
                entry = zipIn.getNextEntry();
            }
            zipIn.close();
        } catch(IOException e){
            Helper.showException(e);
            System.exit(0);
        }
    }

    private static void extractFile(ZipInputStream zipIn, String filePath) throws IOException {
        new File(filePath).getParentFile().mkdirs();
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath));
        byte[] bytesIn = new byte[BUFFER_SIZE];
        int read = 0;
        while ((read = zipIn.read(bytesIn)) != -1) {
            bos.write(bytesIn, 0, read);
        }
        bos.close();
    }
}
