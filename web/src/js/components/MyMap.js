import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';


//#region style
const StMapContainer = styled.div`
  width: 100%;
  height: 100%;
`
//#endregion style

let myMap;
let isFirst = true;

function setPlacemark(lat, lon, bankId) {
  let newPlacemark = new ymaps.Placemark([lat, lon], {
  }, {
    preset: 'islands#icon',
    iconColor: '#0095b6'
  })
  newPlacemark.events.add('click', (e) => {
    let bankEl = document.querySelector(`#bank-${bankId}`);
    let myMenuEl = document.querySelector('#my-menu');
    myMenuEl.classList.add('main-opened');
    bankEl.classList.add('opened');
    bankEl.scrollIntoView();
  })
  myMap.geoObjects.add(newPlacemark)
}

function setRoute(latx, lonx, laty, lony, mode) {
  let multiRoute;
  // if(mode == "auto") {

  // }
  multiRoute = new ymaps.multiRouter.MultiRoute({
    referencePoints: [
      [latx, lonx],
      [laty, lony]
    ],
    params: {
      routingMode: (mode == "auto") ? undefined : (mode == 'social') ? 'masstransit' : 'pedestrian'
    }
  }, 
  {
    boundsAutoApply: true
  });

  myMap.geoObjects.add(multiRoute);
}

const MyMap = ({
  mapsV,
}) => {
  useEffect(() => {
    ymaps.ready(() => {
      myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856],
        zoom: 9
      });
    });
  }, [])


  if(mapsV.banks != []) {
    if(isFirst) {
      isFirst = false;
    } else {
      myMap.geoObjects.removeAll()
    }
    for(let bank of mapsV.banks) {
      setPlacemark(bank.latitude, bank.longitude, bank.id);
    }
  }

  if(mapsV.route != undefined) {
    setRoute(mapsV.route.latx, mapsV.route.lonx, mapsV.route.laty, mapsV.route.lony, mapsV.route.mode);
  }

	return (
    <StMapContainer id="map">
    </StMapContainer>
	);
}

//#region redux
const mapStateToProps = (state) => {
	return {
    mapsV: state.mapsV,
	};
}

const mapDispatchToProps = () => {
	return {
	};
}
//#endregion redux

export default connect(mapStateToProps, mapDispatchToProps)(MyMap);
