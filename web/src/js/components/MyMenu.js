import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';
import axios from 'axios';


//#region style
const StMyMenu = styled.div`
  position: absolute;
  bottom: calc(60px - 60vh);

  width: 100%;
  height: 60vh;

  border-radius: 10px 10px 0 0;
  background-color: #24272f;
  z-index: 1;
  transition: bottom 0.5s;
  
  .name-text {
    position: absolute;
    margin-top: 17px;

    width: 100%;

    text-align: center;
    font-family: 'Roboto', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: #f4f2f3;
  }

  .main-open-close-image {
    position: absolute;
    top: 5px;
    right: 5px;

    width: 50px;
    
    cursor: pointer;
    transform: rotate(-180deg);
    transition: all 0.5s;
  }

  &.main-opened {
    bottom: 0px;
    .main-open-close-image {
      transform: rotate(360deg);
    }
  }
`
const StBanks = styled.div`
  position: absolute;
  top: 60px;

  height: calc(60vh - 80px);
  width: 100%;

  overflow-y: scroll;
  &::-webkit-scrollbar { width: 0; }
  -ms-overflow-style: none;
  overflow: -moz-scrollbars-none;
  scrollbar-width: none;
`
const StBank = styled.div`
  position: relative;
  margin-top: 10px;
  margin-left: 5%;
  height: 60px;
  width: 90%;
  border-radius: 10px;
  background-color: #343945;
  overflow: hidden;
  border-bottom: 20px solid #343945;
  border-top: 20px solid #343945;
  transition: height 0.5s;
  
  .type {
    float: left;
    position: relative;
    width: 35px;
    margin-top: 10px;
    left: 15px;
  } 

  .address {
    width: calc(100% - 105px);
    height: 60px;
    left: 30px;
    position: relative;
    font-size: 15px;
    color: #f4f2f3;
    margin-top: 0px;
    float: left;
  }

  .open-close {
    float: right;
    position: relative;
    width: 40px;
    margin-top: 10px;
    left: 0px;
    cursor: pointer;
    transition: all 0.5s;
  }

  .currencies {
    width: calc(100px);
    left: 30px;
    position: relative;
    font-size: 15px;
    color: #f4f2f3;
    margin-top: 0px;
    font-weight: 700;
    float: left;
  }

  .currency {
    float: left;
    position: relative;
    width: 20px;
    margin-top: 0px;
    left: 0px;
    cursor: pointer;
  }

  .transport-img {
    position: absolute;
    width: 50px;
    font-size: 15px;
    color: #f4f2f3;
    font-weight: 700;
  }

  .transport-text {
    position: absolute;
    font-size: 15px;
    color: #f4f2f3;
    font-weight: 700;
    float: left;
  }

  &.opened {
    height: 220px;
    overflow-y: scroll;
    &::-webkit-scrollbar { width: 0; }
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
    scrollbar-width: none;
    .open-close {
      transform: rotate(540deg);
    }
  }
`

//#endregion style

const MyMenu = ({
  mapsV,
  changeBanks, setRoute,
}) => {

  useEffect(() => {
    ymaps.ready(() => {
      ymaps.geolocation.get({provider: 'browser', mapStateAutoApply: true}).then(geo => {
        axios.post('http://localhost:9002/api/get_points', {
          "latitude": geo.geoObjects.position[0],
          "longitude": geo.geoObjects.position[1],
          "limit": 10,
          "offset": 5,
          "usd_available": true,
          "euro_available": true
        }).then(res => {
          let newBanks = res.data;
          for(let bank of newBanks) {

            bank.autoRoute = { duration: "-", distance: "-" };
            bank.socialRoute = { duration: "-", distance: "-" };
            bank.pedestrianRoute = { duration: "-", distance: "-" };

            let autoRoute = new ymaps.multiRouter.MultiRoute({
              referencePoints: [
                [geo.geoObjects.position[0], geo.geoObjects.position[1]],
                [bank.latitude, bank.longitude]
              ],
              params: {
                avoidTrafficJams: false,
              }
            }, { });
          
            autoRoute.model.events.add('requestsuccess', function() {
              var activeRoute = autoRoute.getActiveRoute();
              bank.autoRoute = { duration: activeRoute.properties.get("duration").text, distance: activeRoute.properties.get("distance").text };
            
              let socialRoute = new ymaps.multiRouter.MultiRoute({
                referencePoints: [
                  [geo.geoObjects.position[0], geo.geoObjects.position[1]],
                  [bank.latitude, bank.longitude]
                ],
                params: {
                  routingMode: 'masstransit'
                }
              }, { });
            
              socialRoute.model.events.add('requestsuccess', function() {
                var activeRoute = socialRoute.getActiveRoute();
                bank.socialRoute = { duration: activeRoute.properties.get("duration").text, distance: activeRoute.properties.get("distance").text };
                let pedestrianRoute = new ymaps.multiRouter.MultiRoute({
                  referencePoints: [
                    [geo.geoObjects.position[0], geo.geoObjects.position[1]],
                    [bank.latitude, bank.longitude]
                  ],
                  params: {
                    routingMode: 'pedestrian'
                  }
                }, { });
              
                pedestrianRoute.model.events.add('requestsuccess', function() {
                  var activeRoute = pedestrianRoute.getActiveRoute();
                  bank.pedestrianRoute = { duration: activeRoute.properties.get("duration").text, distance: activeRoute.properties.get("distance").text };
                  changeBanks(newBanks);
                });
              });
            });
          }
        });
      });
    });
  }, [])

  let banksArr = [];
  for(let bank of mapsV.banks) {
    banksArr.push(<StBank key={bank.id} id={`bank-${bank.id}`}>
      <img className="type" src={bank.type == "office" ? '/assets/img/banks/office.svg' : '/assets/img/banks/ATM.svg'}/>
      <p className='address'>{bank.address}</p>
      <img className="open-close" src="/assets/img/banks/smallOpenClose.svg" onClick={e => {
        let thisClassList = e.target.parentNode.classList;
        if(thisClassList.contains('opened')) {
          thisClassList.remove('opened');
        } else {
          thisClassList.add('opened');
        }
      }}/>
      <p className='currencies'>Валюты: </p>
      <img className='currency' src='/assets/img/banks/currencies/RUB.svg'/>
      { bank.usd_available ? <img className='currency' src='/assets/img/banks/currencies/USD.svg'/> : <div/> }
      { bank.euro_available ? <img className='currency' src='/assets/img/banks/currencies/EUR.svg'/> : <div/> }
      <img className='transport-img' src='/assets/img/banks/auto.svg' style={{left: "20px", top: "105px"}} onClick={e => {
        ymaps.geolocation.get({provider: 'browser', mapStateAutoApply: true}).then(geo => {
          setRoute({ latx: geo.geoObjects.position[0], lonx: geo.geoObjects.position[1], laty: bank.latitude, lony: bank.longitude, mode: "auto" });
        });
      }}/>
      <p className='transport-text' style={{left: "80px", top: "95px"}}>{bank.autoRoute.duration}</p>
      <p className='transport-text' style={{left: "80px", top: "115px"}}>{bank.autoRoute.distance}</p>
      <img className='transport-img' src='/assets/img/banks/social.svg' style={{left: "50%", top: "105px"}} onClick={e => {
        ymaps.geolocation.get({provider: 'browser', mapStateAutoApply: true}).then(geo => {
          setRoute({ latx: geo.geoObjects.position[0], lonx: geo.geoObjects.position[1], laty: bank.latitude, lony: bank.longitude, mode: "social" });
        });
      }}/>
      <p className='transport-text' style={{left: "calc(50% + 60px)", top: "95px"}}>{bank.socialRoute.duration}</p>
      <p className='transport-text' style={{left: "calc(50% + 60px)", top: "115px"}}>{bank.socialRoute.distance}</p>
      <img className='transport-img' src='/assets/img/banks/pedestrian.svg' style={{left: "20px", top: "160px"}} onClick={e => {
        ymaps.geolocation.get({provider: 'browser', mapStateAutoApply: true}).then(geo => {
          setRoute({ latx: geo.geoObjects.position[0], lonx: geo.geoObjects.position[1], laty: bank.latitude, lony: bank.longitude, mode: "pedestrian" });
        });
      }}/>
      <p className='transport-text' style={{left: "80px", top: "150px"}}>{bank.pedestrianRoute.duration}</p>
      <p className='transport-text' style={{left: "80px", top: "170px"}}>{bank.pedestrianRoute.distance}</p>

    </StBank>)
  }

  
	return (
    <StMyMenu id='my-menu'>
      <p className='name-text'>Банкоматы и отделения</p>
      <img className='main-open-close-image' src='/assets/img/banks/openClose.svg'
        onClick={e => {
          let thisClassList = e.target.parentNode.classList;
          if(thisClassList.contains('main-opened')) {
            thisClassList.remove('main-opened');
          } else {
            thisClassList.add('main-opened');
          }
        }}/>
      <StBanks>
        {banksArr}
      </StBanks>
    </StMyMenu>
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
    changeBanks: (value) => { dispatch({ type: 'CHANGE_BANKS', value }); },
    setRoute: (value) => { dispatch({ type: 'SET_ROUTE', value }); },
	};
}
//#endregion redux

export default connect(mapStateToProps, mapDispatchToProps)(MyMenu);
