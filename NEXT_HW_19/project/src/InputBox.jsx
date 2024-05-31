import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
    width: 60%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
    font-size: 16px;

    &:focus {
        border-color: #4caf50;
    }
`;

function InputBox(props) {
    const { value, onChange } = props;
    console.log(props);

    return <StyledInput placeholder="할 일을 추가하세요" type="text" value={value} onChange={onChange} />;
}

export default InputBox;
