adm = Avidemux()
gui = Gui()

# file extension of input files
input_ext = 'mkv'

# file extension for output files
output_ext = 'mkv'

def convert_file(input_file, output_folder):
    output_file = output_folder + '/' + basename(input_file)

    adm.loadVideo(input_file)
    
    # set the video codec
    adm.videoCodec("copy")
    
    adm.audioClearTracks()
    adm.setSourceTrackLanguage(0,"eng")
    adm.audioAddTrack(0)
    
    # set the audio codec
    adm.audioCodec(0, "copy")
    adm.audioSetDrc(0, 0)
    adm.audioSetShift(0, 0,0)
    
    adm.setContainer("MKV", "forceDisplayWidth=False", "displayWidth=1280", "displayAspectRatio=0")
    adm.save(output_file)

def main():
    input_folder = gui.dirSelect("Select the source folder")
    files = get_folder_content(input_folder, input_ext)

    if files is None:
        gui.displayError("Error", "Folder doesn't containt any ." + input_ext " file")
        return 0

    output_folder = gui.dirSelect("Select the output folder")

    for one_file in files:
            convert_file(one_file, output_folder)
    
    print("Done")

main()
