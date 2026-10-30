
"""Modul prapemrosesan citra SIMUTEH."""

import json
import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,
    "gamma": 1.0,
    "clahe_clip": 2.0,
    "clahe_tile": 8,
    "penapis": "median",
    "kernel": 3,
    "sigma": 1.0,
    "tajam_k": 0.0
}


def praproses(img_bgr, p=None):
    p = {**PARAM_BAWAAN, **(p or {})}

    # 1. Resize dengan mempertahankan rasio gambar
    tinggi, lebar = img_bgr.shape[:2]
    lebar_baru = p["lebar"]
    tinggi_baru = round(tinggi * lebar_baru / lebar)

    img = cv2.resize(
        img_bgr,
        (lebar_baru, tinggi_baru),
        interpolation=cv2.INTER_AREA
    )

    # 2. Koreksi gamma
    if p["gamma"] != 1.0:
        gamma = p["gamma"]
        tabel = np.array([
            ((i / 255.0) ** (1.0 / gamma)) * 255
            for i in range(256)
        ]).astype("uint8")

        img = cv2.LUT(img, tabel)

    # 3. CLAHE pada kanal V di ruang warna HSV
    if p["clahe_clip"] > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        clahe = cv2.createCLAHE(
            clipLimit=p["clahe_clip"],
            tileGridSize=(p["clahe_tile"], p["clahe_tile"])
        )

        v = clahe.apply(v)
        img = cv2.cvtColor(
            cv2.merge([h, s, v]),
            cv2.COLOR_HSV2BGR
        )

    # 4. Penapisan derau
    jenis = p["penapis"]
    k = p["kernel"]

    if jenis == "rerata":
        img = cv2.blur(img, (k, k))
    elif jenis == "gaussian":
        img = cv2.GaussianBlur(img, (k, k), p["sigma"])
    elif jenis == "median":
        img = cv2.medianBlur(img, k)
    elif jenis == "none":
        pass

    # 5. Penajaman citra (unsharp masking)
    if p["tajam_k"] > 0:
        blur = cv2.GaussianBlur(img, (0, 0), 1.0)
        img = cv2.addWeighted(
            img, 1 + p["tajam_k"],
            blur, -p["tajam_k"],
            0
        )

    return img


def simpan_param(p, path="hasil/param_praproses.json"):
    parameter = {**PARAM_BAWAAN, **p}

    with open(path, "w") as f:
        json.dump(parameter, f, indent=2)
