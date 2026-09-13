import { z } from "zod";
import { maxChartBytes } from "../shared/attachment";

export interface ChartAttachment {
  data: string;
  mediaType: string;
  name: string;
  filename: string;
}

export async function readAttachment(file: File): Promise<ChartAttachment> {
  if (!["image/png", "image/jpeg", "image/webp"].includes(file.type)) {
    throw new Error("Choose a PNG, JPEG, or WebP chart image.");
  }

  if (file.size > maxChartBytes) {
    throw new Error("Choose an image of 3 MiB or smaller.");
  }

  const data = await new Promise<string>((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const result = z.string().startsWith(`data:${file.type};base64,`).safeParse(reader.result);

      if (result.success) resolve(result.data);
      else reject(new Error("Could not read the image. Choose it again."));
    };

    reader.onerror = () => reject(new Error("Could not read the image. Choose it again."));
    reader.onabort = () => reject(new Error("Image reading stopped. Choose it again."));
    reader.readAsDataURL(file);
  });

  const image = new Image();
  image.src = data;
  await image.decode().catch(() => {
    throw new Error("This file could not be decoded as an image. Choose another image.");
  });

  return {
    data,
    mediaType: file.type,
    name: file.name,
    filename: `${crypto.randomUUID()}-${file.name}`,
  };
}
