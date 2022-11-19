// eslint-disable-next-line no-unused-vars
import { useState, useEffect, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { VscChromeClose, VscDebugRestart, VscDebugStop } from "react-icons/vsc";
import cuid from "cuid";
import "./App.css";

function App() {

  // eslint-disable-next-line no-unused-vars
  const [images, setImages] = useState([])
  const [currentImage, setCurrentImage] = useState()

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.map((file) => {
      const reader = new FileReader();
      const _cuid = cuid()
      reader.onload = function (e) {
        setImages((prevState) => [
          ...prevState,
          { id: _cuid, src: e.target.result, file: file },
        ]);
        setCurrentImage({ id: _cuid, src: e.target.result, file: file })
      };
      reader.readAsDataURL(file);
      return file;
    });
  }, []);
  // eslint-disable-next-line no-unused-vars
  const {getRootProps, getInputProps} = useDropzone({
    accept: 'image/*',
    onDrop: onDrop
  });

  const onImageDelete = (_cuid) => {
    return () => {
      setImages(prevState => prevState.filter(prevItem => prevItem.id !== _cuid))
      setCurrentImage(null)
    }
  }

  return <div className="App relative">
    <div className="text-center text-sm text-gray-700 font-medium cursor-none">Thumbnail Collection</div>
    <section id="image-area">
      <div {...getRootProps({className: 'dropzone flex justify-center items-center my-4 border border-gray-600 border-opacity-50 rounded-md bg-gray-100 aspect-square w-full'})}>
        {/* <div className='absolute top-1 right-1 hover:cursor-pointer focus:cursor-pointer z-10'><button onClick={() => setCurrentImage(null)}><VscChromeClose /></button></div> */}
        <input {...getInputProps()} disabled={!!currentImage} />
        { currentImage ? <img alt="Dropped" src={currentImage.src} className="object-contain"></img> : <p className="text-center text-sm text-gray-700 cursor-none">Drag/Paste image here</p>}
      </div>
    </section>
    <section id="uploaded-images-area" className="my-1 text-gray-700 text-sm">
      {
        images.map(image => (
          <li className="flex justify-between items-center my-1 px-4 border border-gray-600 border-opacity-50 rounded-md bg-green-400 bg-opacity-50" key={image.id}>
            <div className="py-1">{image.file.path} - {image.file.size} bytes</div>
            <button onClick={onImageDelete(image.id)}>
              <VscChromeClose />
            </button>
          </li>
        ))
      }
      <div className="relative flex justify-between items-center my-1 px-4 border border-gray-600 border-opacity-50 rounded-md" style={{background: "linear-gradient(to right, #facc1580, #facc1580 50%, transparent 50%, transparent 100%)"}}>
        <div className="py-1">image001.jpg</div>
        <button>
          <VscDebugStop />
        </button>
      </div>
      <div className="flex justify-between items-center my-1 px-4 border border-gray-600 border-opacity-50 rounded-md bg-green-400 bg-opacity-50">
        <div className="py-1">image002.jpg</div>
        <button>
          <VscChromeClose />
        </button>
      </div>
      <div className="flex justify-between items-center my-1 px-4 border border-gray-600 border-opacity-50 rounded-md bg-red-400 bg-opacity-50">
        <div className="py-1">image003.jpg</div>
        <button>
          <VscDebugRestart />
        </button>
      </div>
    </section>
    <div className="flex justify-center fixed bottom-4 left w-11/12">
      <button className="px-5 py-1 bg-button-primary text-white rounded-md">Upload</button>
    </div>
  </div>;
}

export default App;
