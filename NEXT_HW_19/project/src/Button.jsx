import React from 'react';
import styled from 'styled-components';

const StyledButton = styled.button`
    background-color: #4caf50;
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    &:hover {
        background-color: #45a049;
    }
`;

function Button(props) {
    const { btnName, clickEffect } = props;
    console.log(props);
    return (
        <StyledButton type="button" onClick={clickEffect}>
            {btnName}
        </StyledButton>
    );
}

export default Button;
