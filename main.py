#!/usr/bin/env python3
"""Batch-convert local images with optional resizing."""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

SUPPORTED={".jpg",".jpeg",".png",".webp",".bmp",".tif",".tiff"}

def convert(source:Path,output_dir:Path,fmt:str,quality:int,max_width:int|None)->Path:
    output_dir.mkdir(parents=True,exist_ok=True)
    extension="jpg" if fmt=="jpeg" else fmt
    destination=output_dir/f"{source.stem}.{extension}"
    with Image.open(source) as original:
        image=ImageOps.exif_transpose(original)
        if max_width and image.width>max_width:
            height=max(1,int(image.height*max_width/image.width+0.5))
            image=image.resize((max_width,height),Image.Resampling.LANCZOS)
        if fmt=="jpeg":
            if image.mode not in ("RGB","L"):
                background=Image.new("RGB",image.size,"white")
                if "A" in image.getbands(): background.paste(image,mask=image.getchannel("A"))
                else: background.paste(image.convert("RGB"))
                image=background
            image.save(destination,"JPEG",quality=quality,optimize=True)
        elif fmt=="webp": image.save(destination,"WEBP",quality=quality,method=6)
        else: image.save(destination,"PNG",optimize=True)
    return destination

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path)
    parser.add_argument("--output-dir",type=Path,default=Path("converted"))
    parser.add_argument("--format",choices=("webp","png","jpeg"),default="webp")
    parser.add_argument("--quality",type=int,default=82)
    parser.add_argument("--max-width",type=int)
    parser.add_argument("--recursive",action="store_true")
    args=parser.parse_args()
    if not 1<=args.quality<=100: parser.error("--quality must be between 1 and 100")
    if args.max_width is not None and args.max_width<1: parser.error("--max-width must be positive")
    if not args.input.exists(): parser.error(f"input does not exist: {args.input}")
    if args.input.is_file(): sources=[args.input] if args.input.suffix.lower() in SUPPORTED else []
    else:
        iterator=args.input.rglob("*") if args.recursive else args.input.glob("*")
        sources=[p for p in iterator if p.is_file() and p.suffix.lower() in SUPPORTED]
    if not sources: parser.error("no supported images found")
    for source in sources:
        try: print(f"{source} -> {convert(source,args.output_dir,args.format,args.quality,args.max_width)}")
        except OSError as exc: print(f"SKIP {source}: {exc}")
    return 0

if __name__=="__main__": raise SystemExit(main())
