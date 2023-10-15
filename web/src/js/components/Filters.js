import React, { useRef } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';


//#region style
const StFilters = styled.div`
  position: absolute;
  top: 50px;
  right: -175px;

  width: 200px;
  height: 200px;

  border-radius: 10px 0 0 10px;
  background-color: #24272f;
  z-index: 1;
  transition: right 0.5s;

  &.filters-opened {
    right: 0px;
  }
`
const StImg = styled.img`
  position: absolute;
  top: ${p => p.top};
  left: ${p => p.left};
  width: 50px;
  cursor: pointer;
`
const StBtn = styled.div`
  position: absolute;
  top: ${p => p.top};
  left: 33px;
  width: 130px;
  height: 44px;
  padding: 10px;
  border-radius: 10px;
  background-color: #343945;

  text-align: center;
  font-family: 'Roboto', sans-serif;
  font-size: 15px;
  color: #f4f2f3;
  cursor: pointer;
`
const StCloser = styled.div`
position: absolute;
  top: ${p => p.top};
  left: 10px;
  top: 70px;
  width: 6px;
  height: 60px;
  border-radius: 5px;
  background-color: #dbdbdb;
  cursor: pointer;
`
//#endregion style

const Filters = ({
  mapsV,
  setRoute,
}) => {
  const filters = useRef(null);
  const auto = useRef(null);
  const social = useRef(null);
  const pedestrian = useRef(null);
  let nowChoosed = "auto";

	return (
    <StFilters ref={filters}>
      <StImg src='/assets/img/filters/auto.svg' ref={auto} top="20px" left="30px" onClick={() => {
        auto.current.src = '/assets/img/filters/auto.svg'
        social.current.src = '/assets/img/filters/social-d.svg'
        pedestrian.current.src = '/assets/img/filters/pedestrian-d.svg'
        nowChoosed = "auto";
      }}/>
      <StImg src='/assets/img/filters/social-d.svg' ref={social} top="20px" left="85px" onClick={() => {
        auto.current.src = '/assets/img/filters/auto-d.svg'
        social.current.src = '/assets/img/filters/social.svg'
        pedestrian.current.src = '/assets/img/filters/pedestrian-d.svg'
        nowChoosed = "social";
      }}/>
      <StImg src='/assets/img/filters/pedestrian-d.svg' ref={pedestrian} top="20px" left="140px" onClick={() => {
        auto.current.src = '/assets/img/filters/auto-d.svg'
        social.current.src = '/assets/img/filters/social-d.svg'
        pedestrian.current.src = '/assets/img/filters/pedestrian.svg'
        nowChoosed = "pedestrian";
      }}/>
      <StBtn top={"100px"} onClick={e => {
        let minRoute
        let bankCoord = [55.700562, 37.851807]
        for(let bank of mapsV.banks) {
          let thisRoute = bank[nowChoosed + "Route"].duration.replace("мин", "").replace(" ", "");
          let hours = 0, mins= 0
          if(thisRoute.includes('ч')) {
            hours = Number(thisRoute.split('ч')[0]);
            mins = Number(thisRoute.split('ч')[1]);
          } else {
            mins = Number(thisRoute);
          }
          
          mins = mins + hours * 60
          if(mins < minRoute || minRoute == undefined) {
            minRoute = mins
            bankCoord = [bank.latitude, bank.longitude]
          }
        }
        ymaps.geolocation.get({provider: 'browser', mapStateAutoApply: true}).then(geo => {
          setRoute({ latx: geo.geoObjects.position[0], lonx: geo.geoObjects.position[1], laty: bankCoord[0], lony: bankCoord[1], mode: nowChoosed });
        });
      }}>Скорейший маршрут</StBtn>
      <StCloser onClick={e => {
        let thisClassList = filters.current.classList;
        if(thisClassList.contains('filters-opened')) {
          thisClassList.remove('filters-opened');
        } else {
          thisClassList.add('filters-opened');
        }
      }}/>
    </StFilters>
	);
}

//#region redux
const mapStateToProps = (state) => {
	return {
    mapsV: state.mapsV,
	};
}

const mapDispatchToProps = (dispatch) => {
	return {
    setRoute: (value) => { dispatch({ type: 'SET_ROUTE', value }); },
	};
}
//#endregion redux

export default connect(mapStateToProps, mapDispatchToProps)(Filters);
